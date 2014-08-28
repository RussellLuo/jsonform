#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='jsonform',
    version='0.0.1',
    author='RussellLuo',
    author_email='luopeng.he@gmail.com',
    description=long_description,
    license='MIT',
    long_description=long_description,
    packages=['jsonform'],
    url='https://github.com/RussellLuo/jsonform',
    install_requires=['jsonschema'],
)
