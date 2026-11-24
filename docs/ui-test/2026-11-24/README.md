# Clear Contrast Accessible UI verification

Tested source version 3.8.2 in Obsidian 1.15.1 for Windows on November 24, 2026. The isolated vault contained sample notes, a Canvas board, and a Bases table. Desktop checks used a 1024 × 800 viewport and a 620 px narrow workspace. The mobile editor check used Obsidian's built-in mobile emulation at 390 px.

The [case results](results.json) record live states and contrast ratios measured from computed foreground and background colors in the rendered app. The checks used 4.5:1 for normal text and 3:1 for sampled control boundaries and focus indicators. Coverage is limited to the recorded cases and Windows runtime, including its mobile emulation. [WCAG 2.2 contrast criteria](https://www.w3.org/TR/WCAG22/#contrast-minimum)

## Fixes verified in the app

| Finding in 3.8.1 | Result in 3.8.2 |
| --- | --- |
| Light abstract and tip headings reached 2.08:1, failure and danger headings 3.63:1, and quote headings 2.46:1. | Updated the cyan, red, and quote colors. The 13 tested headings reached at least 6.28:1 in light mode and 8.01:1 in dark mode. The error action uses the updated red and passes text and keyboard focus contrast. |
| A light unresolved link reached 4.11:1 because the host dimmed it. | Unresolved links use a full-strength color and a dotted underline in Reading view and Live Preview. |
| The command palette input lacked a visible focus outline. Its divider reached 1.10:1 in light mode and 1.22:1 in dark mode. | The input uses a higher-contrast border and a keyboard outline in both palettes. Focus outlines also cover keyboard-accessible view header and detached settings controls. |
| Keyboard-selected menu and command rows relied on the fill color. The active tab used the normal tab outline. | Added an inset indicator to selected rows and active tabs. The tab keeps Obsidian's normal outer border. |

## Screenshots

| Screen | Evidence |
| --- | --- |
| Dark Reading view | [Properties, links, callout, and tasks](screens/01-dark-reading.jpg) |
| Light Reading view | [Resolved, external, and unresolved links](screens/02-light-reading.jpg) |
| Dark Live Preview | [Keyboard text selection in the editor](screens/03-dark-live-preview-selection.jpg) |
| Light narrow desktop | [Source mode at 620 px](screens/04-light-narrow-source.jpg) |
| Light callouts | [Warning and error callouts](screens/05-light-warning-and-error-callouts.jpg) |
| Dark command palette | [Filter, focus outline, and selected command](screens/06-dark-command-palette.jpg) |
| Light Appearance settings | [Keyboard focus on a setting](screens/07-light-appearance-settings.jpg) |
| Light file confirmation | [Keyboard focus on the destructive action](screens/08-light-dialog-and-destructive-focus.jpg) |
| Dark Canvas | [Rendered sample cards and connections](screens/09-dark-canvas.jpg) |
| Light Bases | [Rendered sample table](screens/10-light-bases.jpg) |
