#!/usr/bin/env python
import os

from setuptools import find_packages, setup

package_name = "behave-stubs"


def find_stub_files() -> list[str]:
    result = []
    for root, _, files in os.walk(package_name):
        for file in files:
            if file.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


with open("README.md") as f:
    readme = f.read()

dependencies = [
    "behave",
]

setup(
    name=package_name,
    version="0.0.1",
    description="Mypy stubs for Behave",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    license_files=["LICENSE.md"],
    url=f"https://github.com/Elbtalkessel/{package_name}",
    author="Elbtalkessel",
    author_email="rtfsc@pm.me",
    py_modules=[],
    python_requires=">=3.8",
    install_requires=dependencies,
    packages=["behave-stubs", *find_packages()],
    package_data={
        "behave-stubs": find_stub_files(),
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Typing :: Typed",
    ],
)
