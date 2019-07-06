#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Author: Alan Chou 
# Date: 19/6/29
# version: 1.0
# python_version: 3.62

# MIT License
# Copyright (c) 2019 alanzhchou
# email: alanzhchou@gmail.com


from setuptools import setup

import colprint

setup(
    name = 'colprint',
    version = colprint.__version__,
    author = 'alanzhchou',
    author_email = 'alanzhchou@gmail.com',
    url = 'https://github.com/alanzhchou/python_utils/tree/master/colprint',
    description = u'for simply print some colorful hints',
    packages = ['colprint'],
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'colprint_usage=colprint:colprint_usage',
        ]
    }
)
