#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="guolei-py3-51welink",
    version="0.0.1",
    description="a python3 51welink library by guolei",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guolei19850528/guolei_py3_51welink",
    author="guolei",
    author_email="174000902@qq.com",
    license="MIT",
    keywors=["51welink"],
    packages=setuptools.find_packages('./'),
    install_requires=[
        "guolei-py3-requests"
    ],
    python_requires='>=3.0',
    zip_safe=False
)
