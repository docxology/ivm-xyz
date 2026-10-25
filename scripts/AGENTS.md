# `scripts/` — agent reference

## Contract

- Thin orchestrators only: path bootstrap (repository root resolved from `__file__`), logging, and a single delegated call into `tests/` / `ivm_xyz` entrypoints.
- Business/data/plot/analysis logic lives in `ivm_xyz/` and `tests/`; scripts add none.
- Assume **current working directory** = repository root (see [test_runner.py](test_runner.py) which resolves the project root for discovery and writes under `outputs/logs/` and `outputs/reports/`).

## Inventory

| Script | Purpose | Delegates to |
|--------|---------|--------------|
| [test_runner.py](test_runner.py) | Discovers `tests/`, logs to `outputs/logs/`, reports to `outputs/reports/` | `unittest` discovery over `tests/` |
| [generate_comprehensive_report.py](generate_comprehensive_report.py) | Aggregated test / doc report under `outputs/reports/` | `unittest` discovery + [verify_documentation.py](verify_documentation.py) |
| [verify_documentation.py](verify_documentation.py) | Doc vs implementation checks | `ivm_xyz` imports against `docs/API.md`, `README.md`, module structure |

## Commands (from root)

```bash
uv run python scripts/test_runner.py
uv run python scripts/verify_documentation.py
uv run python scripts/generate_comprehensive_report.py
```

## Not packaged

These files are not part of the `ivm_xyz` distribution (`pyproject.toml` excludes `scripts` from the wheel).
