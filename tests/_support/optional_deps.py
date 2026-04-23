"""Optional dependency probes for skipping tests when extras are not installed."""


def _has_matplotlib() -> bool:
    try:
        import matplotlib  # noqa: F401

        return True
    except ImportError:
        return False


HAS_MATPLOTLIB = _has_matplotlib()
