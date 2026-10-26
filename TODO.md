# TODO — ivm-xyz (agent-ergonomics pass, 2026-08-31)

Canonical backlog. One line + path(s) per item. Append new items; mark done items
`[x]` with date; do not delete history.

## Minor

- [x] (2026-08-31) Add version badge (was absent): README now shows 0.2.0, matching `pyproject.toml`. (README.md, pyproject.toml)
- [x] (2026-08-31) Fix stale coverage claim: badge says "99%" without provenance; CI floor is 95% (`.github/workflows/ci.yml:41`). Replaced with floor + verification command. (README.md)
- [x] (2026-08-31) `docs/TESTING_SUMMARY.md` hard-coded per-module test counts (7/8/7...) vs live count 111 passed / 1 skipped — superseded those numbers with a dated, command-verified snapshot. (docs/TESTING_SUMMARY.md)
- [x] (2026-10-24) Resolved by removing redundant `setup.py` — `pyproject.toml` is the single source of packaging truth; updated CI black scope, scripts/AGENTS.md, docs/STRUCTURE.md. (pyproject.toml, .github/workflows/ci.yml)

## Minor (continued)

- [x] (2026-10-25) Removed stale `working/setup.py` (v0.1.0 packaging shim duplicating the metadata deleted from the repo root). (working/setup.py)
- [ ] (2026-10-25) Decide whether the five tracked reference forks under `working/forked_from_SoT/` stay in the index: docs claimed `working/` was entirely unversioned, so the mentions were corrected instead of deleting reference material. (working/forked_from_SoT/, README.md, docs/STRUCTURE.md)

## Medium

- [ ] (2026-10-25) Pick one contract for `.cursor/hooks/state/*.json`: both files are tracked but `.cursor/hooks/state/README.md` calls them gitignored and `AGENTS.md` says "never commit". Either add an ignore rule + `git rm --cached`, or state they are tracked. (.cursor/hooks/state/, .gitignore)
- [ ] (2026-10-25) `docs/STRUCTURE.md` and `docs/DOCUMENTATION_INDEX.md` still describe `Svector` in the "public classes" list while it is not exported from `ivm_xyz` or `ivm_xyz.core.__all__`; decide whether to export it or mark it internal. (docs/STRUCTURE.md, docs/DOCUMENTATION_INDEX.md, ivm_xyz/core/vectors.py)

(Previously no Medium items outstanding; both entries above were found in the 2026-10-25 pass.)

## Major

- [ ] (2026-10-25) Dependency refresh deferred: `uv lock --upgrade` resolved cleanly (numpy 2.5.4, matplotlib 3.11.2, mypy 2.4.0, flake8 7.4.1, coverage 7.17.0, …) but installing the new pins did not finish inside the 10-minute budget on this external drive, so `uv.lock` was restored and the bump is unverified. Re-run `uv sync --all-extras && uv run pytest tests/` on a faster volume before committing it. (uv.lock, pyproject.toml)
- [ ] (2026-10-25) Python support claims stop at 3.13 while the locked dependency set resolves for 3.14/3.15 markers; add 3.14/3.15 to `classifiers`, the CI matrix, and the README badge once a CI run confirms them. (pyproject.toml, .github/workflows/ci.yml, README.md)
- [x] (2026-10-25) Coverage badge has no generator: resolved by stating the CI-enforced floor instead of a dynamic figure — README now reads "coverage 95% floor (CI enforced)" and links the verification command, so nothing claims an unverifiable number. (README.md, .github/workflows/ci.yml)
