# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

from setuptools import find_namespace_packages, setup

setup(
    name="hydra-torch-configs-legacy",
    version="0.9",
    packages=find_namespace_packages(where="./legacy", include=["hydra_configs*"]),
    package_dir={"": "legacy"},
    namespace_packages=["hydra_configs"],
    author=["Omry Yadan", "Rosario Scalise"],
    author_email=["omry@fb.com", "rosario@cs.uw.edu"],
    url="http://github.com/pytorch/hydra-torch",
    include_package_data=True,
)
