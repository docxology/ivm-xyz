"""Optional dependency probes for skipping tests when extras are not installed."""


def _has_matplotlib() -> bool:
    try:
        import matplotlib  # noqa: F401

        return True
    except ImportError:
        return False


def _has_imageio() -> bool:
    try:
        import imageio  # noqa: F401

        return True
    except ImportError:
        return False


HAS_MATPLOTLIB = _has_matplotlib()
HAS_IMAGEIO = _has_imageio()
