# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Security

- Resolved all open Dependabot alerts by upgrading vulnerable (transitive/dev)
  dependencies: `pillow` → 12.3.0, `black` → 26.x, `pytest` → 9.x,
  `fonttools` → 4.63.0.

### Changed

- **Dropped support for Python 3.8 and 3.9** (both end-of-life). The minimum
  supported version is now **Python 3.10**. This was required so the dependency
  resolver could select the patched releases above.

### Added

- Full type hints across the package; `mypy` runs clean and the shipped
  `py.typed` marker is now meaningful.
- GitHub Actions CI: test matrix on Python 3.10/3.11/3.12 with a 95% coverage
  floor, plus a lint/typecheck job (`black`, `flake8`, `mypy`).
- Dependabot configuration for weekly `pip` and `github-actions` updates.
- Pre-commit configuration (`black`, `flake8`, `mypy`, hygiene hooks).
- `tests/test_coverage_gaps.py`, raising line coverage from ~93% to ~99%.

### Fixed

- `PolyhedronPlotter.animate_polyhedron` no longer crashes on matplotlib ≥ 3.10:
  the removed `FigureCanvas.tostring_rgb` API is replaced with `buffer_rgba`.
- Worker-thread exceptions in `animate_polyhedron` are now surfaced instead of
  being silently swallowed by an unconsumed `executor.map`.
- Replaced imageio's deprecated `fps=` argument with `duration=`.

### Removed

- Dead/broken `suppress` branch in `Polyhedron.translate` (it referenced a
  `_suppress` method that exists nowhere and would raise if reached).

## [0.2.0]

- Baseline release: XYZ ↔ IVM conversion, tetrahedron/triangle volume and area,
  polyhedra (Concentric Hierarchy), edge counting, and matplotlib visualization.
