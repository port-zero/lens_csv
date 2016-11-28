#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='lens_csv',
    author='Veit Heller',
    version='0.0.1',
    license='MIT',
    url='https://github.com/port-zero/lens_csv',
    download_url = 'https://github.com/port-zero/lens_csv/tarball/0.0.2',
    description='A CSV parser for lens',
    packages=find_packages('.'),
    install_requires=[
        "pygments",
        "lens-cli",
    ],
)

