"""Setup python project.

References:
    [1] : https://xebia.com/blog/a-practical-guide-to-using-setup-py/
"""
from setuptools import find_packages, setup


setup(
    name="install-registry",
    packages=find_packages(include=["experiment"]),
    version='0.1.0',
)
