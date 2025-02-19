#!/usr/bin/env python3
from setuptools import find_packages, setup

long_description = open("README.md", "r").read()

setup(
    name="serab_byols",
    description="Data-driven Audio Representation 2021",
    author="Logitech",
    author_email="gasser.elbanna@epfl.ch",
    url="",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "",
        "Source Code": "",
    },
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.7"
)

