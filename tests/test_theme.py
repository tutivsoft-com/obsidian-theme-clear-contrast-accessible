import json
import re
import unittest
from pathlib import Path

import tinycss2


ROOT = Path(__file__).resolve().parents[1]
FOCUS_SCOPE = (".workspace-leaf-content", ".view-header", ".modal", ".is-popout-modal", ".menu")


def rgb(value):
    if re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        return tuple(int(value[index:index + 2], 16) / 255 for index in (1, 3, 5))

    mix = re.fullmatch(r"color-mix\(in srgb, (#[0-9a-fA-F]{6}) (\d+)%, (#[0-9a-fA-F]{6})\)", value)
    if mix is None:
        raise ValueError(f"Unsupported palette color: {value}")
    first, percent, second = mix.groups()
    weight = int(percent) / 100
    return tuple(a * weight + b * (1 - weight) for a, b in zip(rgb(first), rgb(second)))


def luminance(color):
    red, green, blue = (
        channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
        for channel in rgb(color)
    )
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


class ThemeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css = (ROOT / "theme.css").read_text(encoding="utf-8")
        cls.rules = {}
        for rule in tinycss2.parse_stylesheet(cls.css, skip_comments=True, skip_whitespace=True):
            if rule.type != "qualified-rule":
                raise AssertionError(f"Unexpected stylesheet rule: {rule}")
            declarations = tinycss2.parse_blocks_contents(
                rule.content, skip_comments=True, skip_whitespace=True
            )
            for declaration in declarations:
                if declaration.type != "declaration":
                    raise AssertionError(f"Invalid declaration: {declaration}")
            # All selector lists in this stylesheet use top-level commas.
            selectors = tinycss2.serialize(rule.prelude).strip().split(",")
            for selector in selectors:
                cls.rules.setdefault(selector.strip(), {}).update(
                    (declaration.name, tinycss2.serialize(declaration.value).strip())
                    for declaration in declarations
                )
        cls.palettes = {mode: cls.rules[f"body.theme-{mode}"] for mode in ("light", "dark")}

    def assert_contrast(self, foreground, background, minimum):
        dimmer, brighter = sorted((luminance(foreground), luminance(background)))
        ratio = (brighter + 0.05) / (dimmer + 0.05)
        self.assertGreaterEqual(
            ratio, minimum, f"{foreground} on {background}: {ratio:.2f}:1, expected {minimum}:1"
        )

    def test_manifest_matches_source_version(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        for key in ("version", "minAppVersion"):
            self.assertRegex(manifest[key], r"^\d+\.\d+\.\d+$")
        self.assertIn(f"/* {manifest['name']} {manifest['version']}. MIT. */", self.css)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"Source version {manifest['version']}.", readme)

    def test_text_is_readable_on_theme_surfaces(self):
        pairs = {
            "--background-primary": (
                "--text-normal", "--text-muted", "--text-faint", "--link-color", "--link-external-color",
            ),
            "--background-secondary": ("--nav-item-color", "--tab-text-color", "--text-faint"),
            "--background-modifier-hover": ("--nav-item-color",),
            "--background-modifier-active-hover": ("--nav-item-color-active",),
            "--text-selection": ("--text-normal", "--link-color", "--link-external-color"),
            "--text-highlight-bg": ("--text-normal", "--link-color", "--link-external-color"),
            "--code-background": (
                "--code-normal", "--code-comment", "--code-function", "--code-keyword", "--code-string",
            ),
            "--interactive-accent": ("--text-on-accent",),
            "--interactive-accent-hover": ("--text-on-accent",),
        }
        for mode, palette in self.palettes.items():
            for surface, text_colors in pairs.items():
                for text_color in text_colors:
                    with self.subTest(mode=mode, surface=surface, text_color=text_color):
                        self.assert_contrast(palette[text_color], palette[surface], 4.5)

    def test_keyboard_focus_contrasts_with_neutral_and_accent_controls(self):
        for scope in FOCUS_SCOPE:
            focus = self.rules[f"{scope} :focus-visible"]
            self.assertRegex(focus["outline"], r"^2px solid var\(--[\w-]+\)$")
            self.assertEqual(focus["outline-offset"], "-2px")
            neutral_token = re.search(r"var\((--[\w-]+)\)", focus["outline"])[1]
            accent_focus = self.rules.get(f"{scope} button.mod-cta:focus-visible", {})
            accent_token = accent_focus.get("outline-color", f"var({neutral_token})")[4:-1]

            for mode, palette in self.palettes.items():
                for surface in ("--background-primary", "--background-secondary"):
                    with self.subTest(scope=scope, mode=mode, surface=surface):
                        self.assert_contrast(palette[neutral_token], palette[surface], 3)
                for surface in ("--interactive-accent", "--interactive-accent-hover", "--color-red"):
                    with self.subTest(scope=scope, mode=mode, surface=surface):
                        self.assert_contrast(palette[accent_token], palette[surface], 3)

    def test_links_are_underlined_in_reading_and_editing(self):
        for selector in (".markdown-rendered a", ".cm-hmd-internal-link", ".cm-link"):
            with self.subTest(selector=selector):
                self.assertIn("underline", self.rules[selector]["text-decoration-line"].split())

    def test_unresolved_links_keep_full_contrast_with_a_distinct_underline(self):
        links = self.rules["body"]
        self.assertEqual(links["--link-unresolved-opacity"], "1")
        self.assertEqual(links["--link-unresolved-decoration-style"], "dotted")
        self.assertEqual(links["--link-unresolved-decoration-color"], "var(--link-unresolved-color)")

    def test_callout_titles_contrast_with_tinted_backgrounds(self):
        self.assertEqual(self.rules["body"]["--callout-quote"], "var(--text-muted)")
        for mode, palette in self.palettes.items():
            for token in ("--color-cyan", "--color-red", "--text-muted"):
                foreground = palette[token]
                background = f"color-mix(in srgb, {foreground} 10%, {palette['--background-primary']})"
                with self.subTest(mode=mode, token=token):
                    self.assert_contrast(foreground, background, 4.5)

    def test_prompt_input_and_keyboard_selection_have_visible_indicators(self):
        self.assertEqual(
            self.rules["input.prompt-input:focus-visible"]["outline"],
            "2px solid var(--text-accent)",
        )
        self.assertEqual(
            self.rules["input.prompt-input"]["border-bottom-color"],
            "var(--background-modifier-border)",
        )
        for selector in (
            ".prompt .suggestion-item.is-selected",
            ".menu-item.selected",
            ".workspace-tab-header-container .workspace-tab-header.is-active",
        ):
            with self.subTest(selector=selector):
                self.assertIn("var(--text-accent)", self.rules[selector]["box-shadow"])
        for mode, palette in self.palettes.items():
            with self.subTest(mode=mode):
                self.assert_contrast(palette["--text-accent"], palette["--background-modifier-hover"], 3)
                self.assert_contrast(palette["--background-modifier-border"], palette["--background-primary"], 3)


if __name__ == "__main__":
    unittest.main()
