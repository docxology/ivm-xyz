# TODO — ivm-xyz (agent-ergonomics pass, 2026-08-31)

Canonical backlog. One line + path(s) per item. Append new items; mark done items
`[x]` with date; do not delete history.

## Minor

- [x] (2026-08-31) Add version badge (was absent): README now shows 0.2.0, matching `pyproject.toml`. (README.md, pyproject.toml)
- [x] (2026-08-31) Fix stale coverage claim: badge says "99%" without provenance; CI floor is 95% (`.github/workflows/ci.yml:41`). Replaced with floor + verification command. (README.md)
- [x] (2026-08-31) `docs/TESTING_SUMMARY.md` hard-coded per-module test counts (7/8/7...) vs live count 111 passed / 1 skipped — superseded those numbers with a dated, command-verified snapshot. (docs/TESTING_SUMMARY.md)
- [x] (2026-10-24) Resolved by removing redundant `setup.py` — `pyproject.toml` is the single source of packaging truth; updated CI black scope, scripts/AGENTS.md, docs/STRUCTURE.md. (pyproject.toml, .github/workflows/ci.yml)

## Medium

None outstanding (was: none found beyond the above).

## Major

- [ ] Coverage badge has no generator: the "99%" figure is not reproducible by any in-repo command. If real coverage matters for the badge, either add a coverage-refresh step to `scripts/generate_comprehensive_report.py` or drop the dynamic badge. (README.md, scripts/generate_comprehensive_report.py)
