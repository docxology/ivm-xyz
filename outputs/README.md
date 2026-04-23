# `outputs/`

All **default** generated artifacts for this repository should land under this tree (not the repository root, not ad-hoc `images/` for new work since v0.2.0). Contents are **gitignored** by default; this file is the only tracked path so clones see the contract.

| Subfolder | Role |
|-----------|------|
| `plots/` | Default for [PolyhedronPlotter](../ivm_xyz/visualization/plotter.py) (`output_folder` default `outputs/plots`); `plots/orchestrators/` is used by [examples/orchestrators/orch_plot_polyhedron.py](../examples/orchestrators/orch_plot_polyhedron.py) |
| `logs/` | e.g. [scripts/test_runner.py](../scripts/test_runner.py) log file |
| `reports/` | e.g. `test_report.txt` and [generate_comprehensive_report.py](../scripts/generate_comprehensive_report.py) output |

**Override the base name:** set environment variable `IVM_XYZ_OUTPUT_ROOT` to an absolute or repo-relative path; examples resolve it in [../examples/orchestrators/config.py](../examples/orchestrators/config.py).

**Library behavior:** The plotter still accepts any `output_folder` string; the default is `outputs/plots` relative to the process current working directory when you construct `PolyhedronPlotter()` with no argument.

The historical [`images/`](../images/) directory remains documented for projects that pass `output_folder="images"` explicitly (v0.1 and older defaults).
