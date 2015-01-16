#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

description = 'Form validation for JSON-like data (i.e. document) in Python.'

setup(
    name='JsonForm',
    version='0.0.2',
    author='RussellLuo',
    author_email='luopeng.he@gmail.com',
    maintainer='RussellLuo',
    maintainer_email='luopeng.he@gmail.com',
    description=description,
    license='MIT',
    long_description=description,
    packages=find_packages(),
    url='https://github.com/RussellLuo/jsonform',
    install_requires=['jsonschema'],
)
