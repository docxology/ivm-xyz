# `examples/` — agent reference

## Files

- [basic_usage.py](basic_usage.py) — multi-topic demo; **no optional deps** beyond `numpy` / the package. Subprocess-executed by [tests/test_integration_comprehensive.py](../tests/test_integration_comprehensive.py) (`PYTHONPATH=.`).
- [visualization_examples.py](visualization_examples.py) — **`[visualization]`** extra: matplotlib, imageio (for GIF in `example_animation`). Uses default `PolyhedronPlotter` output `outputs/plots` (v0.2+).

## `orchestrators/`

Thin, single-purpose scripts ([orchestrators/README.md](orchestrators/README.md)):

- **Paths:** [orchestrators/config.py](orchestrators/config.py) — `IVM_XYZ_OUTPUT_ROOT` (default `outputs` at repo root); orchestrator PNGs go under `<root>/plots/orchestrators/`.
- **Core / polyhedra only:** `orch_constants.py`, `orch_conversion_roundtrip.py` (`--check`), `orch_tetra_pipeline.py`, `orch_triangle_make_tri.py` (`--check`), `orch_triangle_class.py`, `orch_vector_rotation.py`, `orch_core_tetra_vs_polyhedra.py`, `orch_polyhedra_transforms.py`, `orch_platonic_inventory.py`, `orch_edge_counting.py`
- **Optional viz:** `orch_plot_polyhedron.py` (matplotlib; `--output-dir` optional)

Changes should stay aligned with [../README.md](../README.md) and [../docs/API.md](../docs/API.md).
