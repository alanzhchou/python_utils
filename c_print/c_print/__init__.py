#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan Chou 
# Date: 19/6/30
# version: 1.0
# python_version: 3.62

# MIT License
# Copyright (c) 2019 alanzhchou
# email: alanzhchou@gmail.com


from c_print.cprint import *

"""
    This module is for simply print some colorful hints.
"""

__version__ = "0.1"


def c_print_usage():
    print('''
    style in this module:
    _ => underline
    / => italic (may not support)
    + => bold

    color in this module:
    aB => a for front_text, B for background

    # front
    d => dark
    w => white
    g => green (success)
    b => blue (infomation)
    o => orange (warning)
    r => red (error)

    # background
    D => dark
    W => white
    G => green (success)
    B => blue (infomation)
    O => orange (warning)
    R => red (error)

    example for
    => "+gD"
    => "bold front_text is <code>'green'</code> and background is <code>'dark'</code>"
    ''')