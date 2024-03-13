from setuptools import setup, find_packages

setup(
    name='ivm-xyz',
    version='0.1.0',
    description='Convert between XYZ and IVM geometric spaces',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
)