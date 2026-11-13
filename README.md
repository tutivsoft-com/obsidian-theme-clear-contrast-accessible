# Clear Contrast Accessible

An Obsidian theme that keeps secondary text, navigation and controls clearly readable.

**Status: planning only. No theme code has been written.**

Plan date: 13 November 2026. This repository currently contains this planning README only. The name is a descriptive working name; Community name availability must be checked before any future submission.

Search keywords: Obsidian theme, high contrast, accessibility, readable menus, visible controls.

## Who this is for

People who struggle with faint metadata, tiny dim labels and poorly separated controls.

## User need and evidence

Users complain that attractive themes make secondary text and interface elements too faint, especially when their vision is not perfect.

- [Complaints about insufficient contrast](https://www.reddit.com/r/ObsidianMD/comments/1vb0kp3/what_are_people_liking_these_days_themewise/)

The Reddit links come from the preceding idea research and represent qualitative demand, not a market-size estimate or proof that existing themes do not solve the problem. For Pure OLED Rainbow, the additional requirement comes directly from the owner. Other themes and snippets may already address parts of these needs.

## Planned appearance and features

- Keep metadata, menus, bullets, inactive tabs, settings descriptions and property labels readable.
- Offer both light and dark palettes with clear borders and visible keyboard focus.
- Distinguish links, errors, warnings and selections through more than colour alone where the interface allows.
- Use a target of WCAG AA text contrast: 4.5:1 for normal text and 3:1 for large text; check relevant controls too.
- Avoid washed-out disabled states that erase useful labels and avoid decorative transparency over text.

## Mode scope

Plan both light and dark modes. Neither mode is verified yet.

## Future implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Build the theme only after Rahul authorises implementation. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

Official references for later implementation:

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

These are future work items. No release, installation instructions, compatibility certification or Community listing is being claimed by this planning repository.

## Acceptance checklist for later implementation

- [ ] Measure actual foreground/background pairs across representative screens.
- [ ] Test keyboard focus, hover, selection, menus and dialogs.
- [ ] Do not claim full accessibility compliance from a palette check alone.
- [ ] Confirm every claimed feature has been implemented and tested before replacing the planning-only status.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.

## Current boundary

Only repository creation and this Markdown plan are authorised in this task. Do not add theme CSS, manifests, screenshots, release tags or submissions as part of this planning work. Future work stays on this repository's verified primary branch.
