# IVM-XYZ — repository agent notes

## Canonical technical reference

Use **[docs/AGENTS.md](docs/AGENTS.md)** for module layout, utility scripts, workflows, and dependency notes. This file is a short index so tools and contributors land in the right place.

## Layout

| Path | Role |
|------|------|
| [ivm_xyz/](ivm_xyz/) | Installable package (see per-subpackage `AGENTS.md`) |
| [tests/](tests/) | `unittest` suite; visualization tests skip without `matplotlib` |
| [scripts/](scripts/) | Test runner, doc checks, reports |
| [examples/](examples/) | Runnable examples |
| [docs/](docs/) | API, modules, structure, testing |
| [archive/](archive/) | Legacy reference only; not part of the published API |
| [outputs/](outputs/) | Default generated tree: `plots/`, `logs/`, `reports/` (v0.2+; gitignored except [outputs/README.md](outputs/README.md)) |
| [images/](images/) | Optional if you set `output_folder="images"`; v0.1 default. `*.png` / `*.gif` gitignored when written here |
| `working/` | Local scratch (gitignored); only the reference forks in `working/forked_from_SoT/` are tracked |

## Tests

```bash
# From repository root (required for scripts/test_runner.py)
uv sync --all-extras
uv run pytest tests/
# or
uv run python -m unittest discover tests
```

Visualization and any import of `ivm_xyz.visualization` require **matplotlib** (optional extra `visualization` in [pyproject.toml](pyproject.toml)).

## Packaging

- Metadata: [pyproject.toml](pyproject.toml) (authoritative for `[project]`).
- License: [LICENSE](LICENSE) (MIT).

## Documentation index

[docs/DOCUMENTATION_INDEX.md](docs/DOCUMENTATION_INDEX.md)

## Generated artifacts (local only)

[scripts/test_runner.py](scripts/test_runner.py) writes `outputs/logs/test_results.log` and `outputs/reports/test_report.txt`. [scripts/generate_comprehensive_report.py](scripts/generate_comprehensive_report.py) writes `outputs/reports/COMPREHENSIVE_TEST_REPORT.md`. The [outputs/](outputs/) tree is gitignored except [outputs/README.md](outputs/README.md). Set `IVM_XYZ_OUTPUT_ROOT` in examples to relocate generated examples (see [examples/orchestrators/config.py](examples/orchestrators/config.py)). **v0.2.0** changes the default `PolyhedronPlotter` output directory to `outputs/plots/`.

## Learned User Preferences

- Prefer behavioral tests without mocks; optional visualization work should skip or use extras instead of failing at import.
- When executing an attached multi-step plan, do not edit the plan file; drive existing todos from in_progress through completed without recreating them.
- On documentation and examples work, expect thorough passes across `docs/` and thin, composable orchestrator examples under `examples/`.
- Prefer install and test workflows with **uv** from the repository root (`uv sync`, `uv run`).
- Prefer configurable pipelines with analytical checks, clear documentation, and default artifacts under category subfolders of a top-level `outputs/` tree unless overridden.

## Learned Workspace Facts

- `docs/AGENTS.md` is the long-form agent guide; this root file is the short index and entry point for tools.
- `ivm_xyz.visualization` loads **matplotlib** at import time; tests gate on `tests/_support/optional_deps.HAS_MATPLOTLIB`.
- `working/` is gitignored for new files, but five reference forks under `working/forked_from_SoT/` are tracked in the index (outside the lint/format surface, like `archive/`).
- `scripts/test_runner.py` resolves the repository root, switches cwd there for discovery, and writes logs and reports under `outputs/logs/` and `outputs/reports/`.
- `PolyhedronPlotter` and library defaults use **`outputs/plots/`**; **`images/`** is only for explicit legacy overrides.
