#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       : setup
@Author     : alanzhchou
@Create     : 19/7/12-1:33
@Python     : 3.62
@Version    : 1.0
@Email      : alanzhchou@gmail.com
@Copyright  : MIT License - Copyright (c) 2019 alanzhchou
@description:

@Change log :
19/7/12-1:33 created
"""

from setuptools import setup
import codetoolbox


setup(
    name = codetoolbox.name,
    version = codetoolbox.version,
    author = 'alanzhchou',
    author_email = 'alanzhchou@gmail.com',
    url = 'https://github.com/alanzhchou/python_utils/tree/master/imgtoolbox',
    description = u'''this module for some code file processing such as calculate lines of code files''',
    packages = ['codetoolbox'],
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'codetoolbox=codetoolbox:command_line_function',
        ]
    }
)