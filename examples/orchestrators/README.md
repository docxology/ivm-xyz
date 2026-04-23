# Thin orchestrator examples

Ten small scripts (numpy only) plus one optional matplotlib demo: each file is a single `main()` workflow, runnable from the **repository root**:

```bash
uv run python examples/orchestrators/<script>.py
```

**Output root:** [config.py](config.py) reads `IVM_XYZ_OUTPUT_ROOT` (default `outputs` under the repository root) and places orchestrator plots under `…/plots/orchestrators/`.

**Analytical checks:** [orch_conversion_roundtrip.py](orch_conversion_roundtrip.py) and [orch_triangle_make_tri.py](orch_triangle_make_tri.py) support `--rtol` / `--atol` and `--check` to exit with status 1 on tolerance failure. For triangle areas, IVM and XYZ are related by the package constant `S3` (see [docs/MODULES.md](../../docs/MODULES.md), [docs/BACKGROUND.md](../../docs/BACKGROUND.md)); `make_tri` uses edge lengths `|v0|`, `|v1|`, `|v1-v0|`, not the parallelogram cross product.

| Script | Purpose | Dependencies |
|--------|---------|--------------|
| [orch_constants.py](orch_constants.py) | Print `D`, `R`, `PHI`, `ROOT*`, `S3` | core only |
| [orch_conversion_roundtrip.py](orch_conversion_roundtrip.py) | Scalar XYZ↔IVM and `Vector`↔`Qvector`; optional `--check` | core + conversion |
| [orch_tetra_pipeline.py](orch_tetra_pipeline.py) | `make_tet` on a few vector triples | core |
| [orch_triangle_make_tri.py](orch_triangle_make_tri.py) | `make_tri` from two `Vector`s; optional `--check` vs Heron | core |
| [orch_triangle_class.py](orch_triangle_class.py) | `Triangle` from three edge lengths; IVM/XYZ area | core |
| [orch_vector_rotation.py](orch_vector_rotation.py) | `Vector.rotz` / `roty`, `unit()` | core |
| [orch_core_tetra_vs_polyhedra.py](orch_core_tetra_vs_polyhedra.py) | `core.Tetrahedron` (edges) vs `PolyTetrahedron` (solid) | core + polyhedra |
| [orch_polyhedra_transforms.py](orch_polyhedra_transforms.py) | `Cube` scale and translate; shows vertex move | polyhedra |
| [orch_platonic_inventory.py](orch_platonic_inventory.py) | All exported Platonic types: volume / counts | polyhedra |
| [orch_edge_counting.py](orch_edge_counting.py) | `tet_edges`, `oct_edges`, `cubocta_*` for f=1..4 | polyhedra |
| [orch_plot_polyhedron.py](orch_plot_polyhedron.py) | `Cube` → PNG under `outputs/.../orchestrators` (override `--output-dir`) | `matplotlib` (`[visualization]`) |

**Library default (v0.2.0):** [PolyhedronPlotter](../../ivm_xyz/visualization/plotter.py) saves to `outputs/plots` when `output_folder` is omitted.

The bundled [basic_usage.py](../basic_usage.py) remains the main multi-topic demo; [visualization_examples.py](../visualization_examples.py) uses the v0.2 default directory.

See [../AGENTS.md](../AGENTS.md) for the examples folder map.
