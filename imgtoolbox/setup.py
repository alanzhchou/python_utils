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
    url = 'https://github.com/alanzhchou/python_utils/tree/master/imgtoolbox',
    description = u'''this module for some img processing util such as generate icon from input img
                convert img into ascii char img, using "imgtoolbox -h" for more info''',
    packages = ['imgtoolbox'],
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'imgtoolbox=imgtoolbox:command_line_function',
        ]
    }
)


