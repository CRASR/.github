# Contributing to CRASR projects

Thanks for your interest. These guidelines apply to every CRASR repository unless the repo has its own `CONTRIBUTING.md`.

## Before you start

- **Open an issue first** for anything beyond a small fix, so we can agree on the approach before you put in the work.
- Check the repo's README for setup steps, data requirements, and any project-specific conventions.

## Making changes

1. Fork the repo (or create a branch if you're a CRASR member).
2. Keep each pull request focused on one change.
3. Describe what changed and why, and link the related issue.
4. Make sure the code runs and any existing tests or checks pass.

## Code style

- **R:** follow the [tidyverse style guide](https://style.tidyverse.org/). Prefer the native pipe (`|>`), and document exported functions with roxygen2.
- **Python:** follow PEP 8.
- Write comments that explain *why*, not *what*.

## Data and credentials

- Never commit passwords, API keys, tokens, or connection strings. Keep them in `.Renviron`, `.env`, or a secrets manager, and make sure those files are git-ignored.
- Don't commit raw data that is unpublished, restricted by an agreement, or contains personal information. Ask a maintainer if you're unsure.

## AI-assisted contributions

If AI tools helped write your contribution, say so in the pull request. If the repo keeps an AI-use log, add an entry there.

## Conduct

All contributors are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md).
