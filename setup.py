import os
import re
import sys
from distutils.core import Command

from setuptools import find_packages, setup


_deps = [
    "Pillow",
    "huggingface-hub",
    "python>=3.8.0",
    "requests",
    "torch",
    "diffusers",
    "transformers>=4.25.1",
    "urllib3",
    "googletrans==3.1.0a0",
    "numpy",
]

deps = {b: a for a, b in (re.findall(r"^(([^!=<>~]+)(?:[!=<>~].*)?$)", x)[0] for x in _deps)}



def deps_list(*pkgs):
    return [deps[pkg] for pkg in pkgs]


class DepsTableUpdateCommand(Command):
    """
    A custom distutils command that updates the dependency table.
    usage: python setup.py deps_table_update
    """

    description = "build runtime dependency table"
    user_options = [
        # format: (long option, short option, description).
        (
            "dep-table-update",
            None,
            "updates api/dependency_versions_table.py",
        ),
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        entries = "\n".join([f'    "{k}": "{v}",' for k, v in deps.items()])
        content = [
            "# THIS FILE HAS BEEN AUTOGENERATED. To update:",
            "# 1. modify the `_deps` dict in setup.py",
            "# 2. run `make deps_table_update`",
            "deps = {",
            entries,
            "}",
            "",
        ]
        target = "api/dependency_versions_table.py"
        print(f"updating {target}")
        with open(target, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(content))




install_requires = [
    deps["Pillow"],
    deps["diffusers"],
    deps["transformers"],
    deps["requests"],
    deps["huggingface-hub"],
    deps["torch"],
    deps["urllib3"],
]




version_range_max = max(sys.version_info[1], 10) + 1

setup(
    name="Auto_diffusers",
    version="0.1.0",
    description="Customized diffusers with model search and other functions.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="diffusers_in_Colab for another platform",
    license="BSD 3-Clause License",
    author="suzukimain(https://github.com/suzukimain)",
    author_email="subarucosmosmain@gmail.com",
    url="https://github.com/suzukimain/Auto_diffusers",
    package_dir={"": "src"},
    packages=find_packages("src"),
    package_data={"": ["py.typed"]},
    include_package_data=True,
    install_requires=list(install_requires),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
    ]
    + [f"Programming Language :: Python :: 3.{i}" for i in range(8, version_range_max)],
    cmdclass={"deps_table_update": DepsTableUpdateCommand},
)
