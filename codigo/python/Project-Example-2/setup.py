#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("requirements.txt") as f:
    requirements = [req.strip() for req in f.readlines()]

test_requirements = [
    "nose",
    "coverage",
    "mock",
    "coveralls",
    "flake8"
]

setup(
    name='Project-Name',
    description="Template for a simple python project.",
    packages=[
        'package_name'
    ],
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3+",
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=test_requirements
)
