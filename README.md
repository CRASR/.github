# CRASR/.github

Organization-wide settings and defaults for [CRASR](https://github.com/CRASR).

| Path | What it does |
|---|---|
| `profile/README.md` | The public profile shown at the top of github.com/CRASR |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md` | Default community files for every CRASR repo that doesn't have its own |
| `.github/ISSUE_TEMPLATE/`, `.github/pull_request_template.md` | Default issue forms and PR template, used by repos without their own |
| `assets/banner/` | Profile banners (light and dark), PNG for display plus SVG source |
| `assets/logo/` | CRASR logo (SVG, plus 512 and 1024 px PNG) |
| `assets/social-preview/` | Template and R script for repo social-preview images |
| `assets/src/` | Python generator for the logo, banners, and template |

## Brand colors

| | Hex |
|---|---|
| Baylor Green | `#154734` |
| University Gold | `#FFB81C` |
| Water-column mid green | `#1E5C44` |
| Water-column deep green | `#0C2E21` |

Type: [Inter](https://rsms.me/inter/) / Inter Display.

## Social preview images

Each public repo can have a 1280×640 image that appears when its link is shared. To make one:

```sh
cd assets/social-preview
Rscript make-social-preview.R gage-widget "A desktop widget for live USGS stream gage readings"
```

Then upload the PNG under the repo's **Settings → General → Social preview**. Requires the `rsvg` R package. Install Inter for the intended look; otherwise a system sans-serif is used.
