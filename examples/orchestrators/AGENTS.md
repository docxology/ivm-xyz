# orchestrators/ — Agent Notes

Eleven thin-orchestrator demo scripts (`orch_*.py`) + `config.py` + `README.md`
(verified 2026-08-29). Each script is a single `main()` workflow runnable from the
repo root: `uv run python examples/orchestrators/<script>.py`. `config.py` reads
`IVM_XYZ_OUTPUT_ROOT` (default `outputs/` at repo root); plots land under
`outputs/plots/orchestrators/`. Two scripts (`orch_conversion_roundtrip.py`,
`orch_triangle_make_tri.py`) support `--rtol/--atol/--check` and exit 1 on
tolerance failure. Stdlib + `ivm_xyz` only; one optional matplotlib demo.
