# `scripts/`

Developer utilities. **Run from the repository root** so paths resolve (`tests/`, `examples/`, reports).

| Script | Purpose | Delegates to | Command |
|--------|---------|--------------|---------|
| [test_runner.py](test_runner.py) | Discovers `tests/`, logs to `outputs/logs/`, reports to `outputs/reports/` | `unittest` discovery over `tests/` | `uv run python scripts/test_runner.py` |
| [generate_comprehensive_report.py](generate_comprehensive_report.py) | Aggregated test / doc report | `unittest` discovery + [verify_documentation.py](verify_documentation.py) | `uv run python scripts/generate_comprehensive_report.py` |
| [verify_documentation.py](verify_documentation.py) | Doc vs implementation checks | `ivm_xyz` imports against `docs/API.md`, `README.md`, module structure | `uv run python scripts/verify_documentation.py` |

See [AGENTS.md](AGENTS.md).
