#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       : setup
@Author     : alanzhchou
@Create     : 19/7/11-23:51
@Python     : 3.62
@Version    : 1.0
@Email      : alanzhchou@gmail.com
@Copyright  : MIT License - Copyright (c) 2019 alanzhchou

@Change log :
19/7/11-23:51 created
"""

from setuptools import setup
import imgtoolbox

setup(
    name = imgtoolbox.name,
    version = imgtoolbox.version,
    author = 'alanzhchou',
    author_email = 'alanzhchou@gmail.com',
    url = 'https://github.com/alanzhchou/python_utils/tree/master/colprint',
    description = u'for simply print some colorful hints',
    packages = ['colprint'],
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'imgtoolbox=imgtoolbox:command_line_function',
        ]
    }
)


