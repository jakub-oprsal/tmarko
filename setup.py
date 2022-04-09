#!/usr/bin/env python3
from setuptools import setup

setup(
        name = 'tmarko',
        version = '0.1',
        description = 'Hack of `marko` markdown parser for LaTeX output',
        author = 'Jakub Opršal',
        author_email = 'jakub.oprsal@cs.ox.ac.uk',
        license = 'MIT',
        py_modules = ['tmarko'],
        install_requires = ['marko']
)
