# .github/ — Agent Notes

GitHub configuration for this repo:

- `dependabot.yml` — automated dependency updates.
- `workflows/ci.yml` — tests, lint/typecheck, and dependency-audit jobs.
- `workflows/codeql.yml` — CodeQL static security analysis.
- `workflows/dependency-review.yml` — PR dependency review.

Keep workflow changes minimal and verify with actionlint-style review; the CI
badge on the root README points at `workflows/ci.yml`.
