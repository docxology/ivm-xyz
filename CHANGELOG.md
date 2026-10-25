# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Security

- Resolved all open Dependabot alerts by upgrading vulnerable (transitive/dev)
  dependencies: `pillow` → 12.3.0, `black` → 26.x, `pytest` → 9.x,
  `fonttools` → 4.63.0.
- Upgraded `pillow` (transitive via matplotlib/imageio) to **13.0.0**, resolving
  Dependabot alert #23 / GHSA-8g5g-8vmr-9782 (CVE-2026-112403, critical heap
  buffer overflow in `ImagingJpegDecode`). No `pillow <= 12.3.0` remains in
  `uv.lock`. An explicit `pillow>=13.0.0` floor now guards the `visualization`
  extra for non-locked installs.

### Changed

- **Dropped support for Python 3.8 and 3.9** (both end-of-life). The minimum
  supported version is now **Python 3.10**. This was required so the dependency
  resolver could select the patched releases above.
- **Dropped support for Python 3.10** (end-of-life 2026-10-31). The minimum
  supported version is now **Python 3.11**. Required because the patched Pillow
  13.0.0 release does not support Python 3.10, and keeping a 3.10 resolution
  marker would have left the vulnerable pillow in `uv.lock`.

### Added

- Full type hints across the package; `mypy` runs clean and the shipped
  `py.typed` marker is now meaningful.
- GitHub Actions CI: test matrix on Python 3.10/3.11/3.12 with a 95% coverage
  floor, plus a lint/typecheck job (`black`, `flake8`, `mypy`).
- Dependabot configuration for weekly `uv` and `github-actions` updates.
- Pre-commit configuration (`black`, `flake8`, `mypy`, hygiene hooks).
- `tests/test_coverage_gaps.py`, raising line coverage from ~93% to ~99%.
- CI hardening: workflow-level least-privilege `permissions`, third-party
  actions pinned to commit SHAs, a `uv lock --check` freshness gate, and a
  `pip-audit` dependency-audit job.
- New `dependency-review` (PR dependency scanning) and `CodeQL` (static
  security analysis) workflows.
- Dependabot now uses the native `uv` ecosystem for `uv.lock`/`pyproject`
  updates instead of the legacy `pip` ecosystem.

### Fixed

- `PolyhedronPlotter.animate_polyhedron` no longer crashes on matplotlib ≥ 3.10:
  the removed `FigureCanvas.tostring_rgb` API is replaced with `buffer_rgba`.
- Worker-thread exceptions in `animate_polyhedron` are now surfaced instead of
  being silently swallowed by an unconsumed `executor.map`.
- Replaced imageio's deprecated `fps=` argument with `duration=`.
- `ivm_xyz/py.typed` is now actually shipped: it was declared in
  `[tool.setuptools.package-data]` but missing from the package directory.
- `[tool.setuptools] packages` now includes the four subpackages, so wheels
  install `ivm_xyz.core`, `ivm_xyz.conversion`, `ivm_xyz.polyhedra` and
  `ivm_xyz.visualization` (previously only the top-level package was listed).
- `scripts/generate_comprehensive_report.py` no longer runs subprocesses
  through the shell (`shell=True` removed; commands are argv lists).

### Removed

- Dead/broken `suppress` branch in `Polyhedron.translate` (it referenced a
  `_suppress` method that exists nowhere and would raise if reached).

## [0.2.0]

- Baseline release: XYZ ↔ IVM conversion, tetrahedron/triangle volume and area,
  polyhedra (Concentric Hierarchy), edge counting, and matplotlib visualization.
