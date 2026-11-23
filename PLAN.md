# Clear Contrast Accessible design plan

An Obsidian theme that keeps secondary text, navigation and controls clearly readable.

This plan records the proposed design as of 13 November 2026. The [README](README.md) describes the implemented theme, its installation and its current source checks.

Search keywords: Obsidian theme, high contrast, accessibility, readable menus, visible controls.

## Who this is for

People who struggle with faint metadata, tiny dim labels and poorly separated controls.

## User need and evidence

Users complain that attractive themes make secondary text and interface elements too faint, especially when their vision is not perfect.

- [Complaints about insufficient contrast](https://www.reddit.com/r/ObsidianMD/comments/1vb0kp3/what_are_people_liking_these_days_themewise/)

The Reddit discussion was part of the original research into readability needs.

## Planned appearance and features

- Keep metadata, menus, bullets, inactive tabs, settings descriptions and property labels readable.
- Offer both light and dark palettes with clear borders and visible keyboard focus.
- Distinguish links, errors, warnings and selections through more than colour alone where the interface allows.
- Use a target of WCAG AA text contrast: 4.5:1 for normal text and 3:1 for large text; check relevant controls too.
- Avoid washed-out disabled states that erase useful labels and avoid decorative transparency over text.

## Mode scope

The original plan included both light and dark modes.

## Original implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Build the theme only after Rahul authorises implementation. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

### Official references

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

## Original acceptance checklist

- [ ] Measure actual foreground/background pairs across representative screens.
- [ ] Test keyboard focus, hover, selection, menus and dialogs.
- [ ] Do not claim full accessibility compliance from a palette check alone.
- [ ] Confirm every claimed feature has been implemented and tested before replacing the planning-only status.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.

## Original scope

The planning task covered creating the repository and recording this design for later implementation.
