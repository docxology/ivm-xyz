# _support/ — Agent Notes

Shared test-support helpers (verified 2026-08-29):

- `fixtures.py` — shared fixture helpers.
- `optional_deps.py` — helpers for tests that skip when optional dependencies
  (e.g. matplotlib) are absent.

Imported by sibling test modules; not a test module itself (no `test_` prefix).
Keep additions generic — package tests live one level up.
