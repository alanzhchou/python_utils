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

import c_print

setup(
    name = 'c_print',
    version = c_print.__version__,
    author = 'alanzhchou',
    author_email = 'alanzhchou@gmail.com',
    url = 'https://github.com/alanzhchou/python_utils',
    description = u'for simply print some colorful hints',
    packages = ['c_print'],
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'c_print_usage=c_print:c_print_usage',
        ]
    }
)
