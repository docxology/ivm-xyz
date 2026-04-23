# `docs/`

Project documentation: API, modules, background, structure, and agent-oriented workflows. Package public API and version live in the repository root [pyproject.toml](../pyproject.toml) and [ivm_xyz/__init__.py](../ivm_xyz/__init__.py).

**Start here:** [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) (topic index and reading paths).

| File | Description |
|------|-------------|
| [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) | Topic / use-case index; maintenance checklist |
| [AGENTS.md](AGENTS.md) | Full agent / developer guide (workflows, paths, `uv`, outputs) |
| [API.md](API.md) | Class and function reference (signatures) |
| [MODULES.md](MODULES.md) | Per-module narrative and `AGENTS` links by subfolder |
| [STRUCTURE.md](STRUCTURE.md) | Tree layout and import examples |
| [TESTING_SUMMARY.md](TESTING_SUMMARY.md) | How to run tests; `outputs/` log/report names |
| [BACKGROUND.md](BACKGROUND.md) | IVM, Synergetics, and volume/area at a high level |
| [TECHNICAL_REFERENCE.md](TECHNICAL_REFERENCE.md) | Algorithms, precision, and implementation notes |
| [.cursorrules](.cursorrules) | House style for contributors and tools (if present) |

**Reading order (typical):** root [../README.md](../README.md) → this index or [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) → [MODULES.md](MODULES.md) or [API.md](API.md) as needed; [BACKGROUND.md](BACKGROUND.md) when the math (IVM vs XYZ, `S3`) needs context.

**Generated (do not hand-edit):** [scripts/generate_comprehensive_report.py](../scripts/generate_comprehensive_report.py) writes [outputs/reports/COMPREHENSIVE_TEST_REPORT.md](../outputs/reports/COMPREHENSIVE_TEST_REPORT.md) (ignored except the [outputs README](../outputs/README.md)). [scripts/test_runner.py](../scripts/test_runner.py) writes [outputs/logs/test_results.log](../outputs/logs) and [outputs/reports/test_report.txt](../outputs/reports).

**Examples and orchestrators:** [../examples/AGENTS.md](../examples/AGENTS.md), [../examples/orchestrators/README.md](../examples/orchestrators/README.md); optional env [IVM_XYZ_OUTPUT_ROOT](AGENTS.md) (see [examples/orchestrators/config.py](../examples/orchestrators/config.py)).

Root [../README.md](../README.md) links here for the narrative quick start. See [AGENTS.md](AGENTS.md) for the same map with workflow commands.
