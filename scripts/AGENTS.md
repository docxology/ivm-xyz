# `scripts/` — agent reference

## Contract

- Assume **current working directory** = repository root (see [test_runner.py](test_runner.py) which resolves the project root for discovery and writes under `outputs/logs/` and `outputs/reports/`).

## Commands (from root)

```bash
uv run python scripts/test_runner.py
uv run python scripts/verify_documentation.py
uv run python scripts/generate_comprehensive_report.py
```

## Not packaged

These files are not part of the `ivm_xyz` distribution (`setup.py` / `pyproject` exclude `scripts` from the wheel).
