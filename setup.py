"""
Setup script for ivm-xyz package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    requirements = requirements_file.read_text().strip().split("\n")
    requirements = [r.strip() for r in requirements if r.strip() and not r.startswith("#")]

setup(
    name="ivm-xyz",
    version="0.1.0",
    description="Convert between XYZ and IVM geometric spaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="IVM-XYZ Contributors",
    author_email="",
    url="https://github.com/docxology/ivm-xyz",
    packages=find_packages(exclude=["tests", "examples", "docs", "working"]),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "visualization": ["matplotlib>=3.0.0", "imageio>=2.0.0"],
        "dev": ["pytest>=7.0.0", "black>=22.0.0", "flake8>=4.0.0"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="geometry, mathematics, tetrahedron, ivm, quadray, synergetics, buckminster fuller",
)

