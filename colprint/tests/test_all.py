#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan Chou 
# Date: 19/4/20
# version: 1.0
# python_version: 3.62

import unittest.runner

test_modules = [
        "tests.test_modules.test_cprint"
    ]



suite = unittest.TestSuite()
for one_module in test_modules:
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName(one_module))

unittest.TextTestRunner().run(suite)
