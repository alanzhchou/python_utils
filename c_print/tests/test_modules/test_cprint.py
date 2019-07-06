#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Author: Alan Chou 
# Date: 19/6/12
# version: 1.0
# python_version: 3.62

# MIT License
# Copyright (c) 2019 alanzhchou
# email: alanzhchou@gmail.com

import unittest

from c_print.cprint import ColorUtilError, CodeQueryError, ColorAndStyle, cprint
from tests.redirect import ListStream, redirect_stdout_to, clear_stdout_redirect


class TestColorPrint(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.list_stream:ListStream = []

    @classmethod
    def tearDownClass(self):
        self.list_stream = None

    def setUp(self):
        self.list_stream = redirect_stdout_to(ListStream, ignore="\n")

    def tearDown(self):
        self.list_stream.clear()
        clear_stdout_redirect()

    def test_setUp(self):
        print("123")
        print("1234")
        print("\t")
        print("\n")
        list_buffer = self.list_stream.get()
        self.assertEqual("123" , list_buffer[0])
        self.assertEqual("1234", list_buffer[1])
        self.assertEqual("\t", list_buffer[2])
        self.assertEqual(len(list_buffer), 3)





    def test_ColorAndFont__get_single_code_success(self):
        '''
        d => dark
        w => white
        g => green (success)
        b => blue (infomation)
        o => orange (warning)
        r => red (error)

        F_DARK = "30"
        F_WHITE = "37"
        F_GREEN = "32"
        F_ORANGE = "33"
        F_BLUE = "34"
        F_RED = "31"
        '''
        self.assertEqual(ColorAndStyle._get_single_code("+"), "1")
        self.assertEqual(ColorAndStyle._get_single_code("/"), "3")
        self.assertEqual(ColorAndStyle._get_single_code("_"), "4")

        self.assertEqual(ColorAndStyle._get_single_code("d"), "30")
        self.assertEqual(ColorAndStyle._get_single_code("w"), "37")
        self.assertEqual(ColorAndStyle._get_single_code("g"), "32")
        self.assertEqual(ColorAndStyle._get_single_code("o"), "33")
        self.assertEqual(ColorAndStyle._get_single_code("b"), "34")
        self.assertEqual(ColorAndStyle._get_single_code("r"), "31")

        self.assertEqual(ColorAndStyle._get_single_code("D"), "40")
        self.assertEqual(ColorAndStyle._get_single_code("W"), "47")
        self.assertEqual(ColorAndStyle._get_single_code("G"), "42")
        self.assertEqual(ColorAndStyle._get_single_code("O"), "43")
        self.assertEqual(ColorAndStyle._get_single_code("B"), "44")
        self.assertEqual(ColorAndStyle._get_single_code("R"), "41")

    def test_ColorAndFont__get_single_code_fail(self):
        self.assertRaises(CodeQueryError, ColorAndStyle._get_single_code, "!")
        self.assertRaises(CodeQueryError, ColorAndStyle._get_single_code, "12345678")




    def test_ColorAndFont__get_ANSI_color_and_style_code_success(self):
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("+"), "\033[1m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("/"), "\033[3m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("_"), "\033[4m")

        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("dD"), "\033[30;40m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("wD"), "\033[37;40m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("gD"), "\033[32;40m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("oD"), "\033[33;40m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("bD"), "\033[34;40m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("rD"), "\033[31;40m")

        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("dW"), "\033[30;47m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("wW"), "\033[37;47m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("gW"), "\033[32;47m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("oW"), "\033[33;47m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("bW"), "\033[34;47m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("rW"), "\033[31;47m")

        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("dG"), "\033[30;42m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("wG"), "\033[37;42m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("gG"), "\033[32;42m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("oG"), "\033[33;42m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("bG"), "\033[34;42m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("rG"), "\033[31;42m")

        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("dO"), "\033[30;43m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("wO"), "\033[37;43m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("gO"), "\033[32;43m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("oO"), "\033[33;43m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("bO"), "\033[34;43m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("rO"), "\033[31;43m")

        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("dB"), "\033[30;44m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("wB"), "\033[37;44m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("gB"), "\033[32;44m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("oB"), "\033[33;44m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("bB"), "\033[34;44m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("rB"), "\033[31;44m")

        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("dR"), "\033[30;41m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("wR"), "\033[37;41m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("gR"), "\033[32;41m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("oR"), "\033[33;41m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("bR"), "\033[34;41m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("rR"), "\033[31;41m")

        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("+dD"), "\033[1;30;40m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("+wD"), "\033[1;37;40m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("+gD"), "\033[1;32;40m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("+oD"), "\033[1;33;40m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("+bD"), "\033[1;34;40m")
        self.assertEqual(ColorAndStyle._get_ANSI_color_and_style_code("+rD"), "\033[1;31;40m")

    def test_ColorAndFont__get_ANSI_color_and_style_code_fail(self):
        self.assertRaises(CodeQueryError, ColorAndStyle._get_ANSI_color_and_style_code, "!")
        self.assertRaises(CodeQueryError, ColorAndStyle._get_ANSI_color_and_style_code, "12345678")




    def test_cprint_success(self):
        cprint("")
        cprint(" ", cs="+")
        cprint(" ", cs="_")
        cprint(" ", cs="/")

        cprint(" ", cs="d")
        cprint(" ", cs="w")
        cprint(" ", cs="g")
        cprint(" ", cs="b")
        cprint(" ", cs="o")
        cprint(" ", cs="r")

        cprint(" ", cs="D")
        cprint(" ", cs="W")
        cprint(" ", cs="G")
        cprint(" ", cs="B")
        cprint(" ", cs="O")
        cprint(" ", cs="R")

        cprint(" ", cs="dD")
        cprint(" ", cs="wW")
        cprint(" ", cs="gG")
        cprint(" ", cs="bB")
        cprint(" ", cs="oO")
        cprint(" ", cs="rR")

        cprint(" ", cs="+dD")
        cprint(" ", cs="/dD")
        cprint(" ", cs="_dD")

        cprint(" ", cs="+", all_line=True)
        cprint(" ", cs="_", all_line=True)
        cprint(" ", cs="/", all_line=True)

        list_buffer = self.list_stream.get()

        self.assertEqual(list_buffer[0], "")
        self.assertEqual(list_buffer[1], "\033[1m \033[0m")
        self.assertEqual(list_buffer[2], "\033[4m \033[0m")
        self.assertEqual(list_buffer[3], "\033[3m \033[0m")

        self.assertEqual(list_buffer[4], "\033[30m \033[0m")
        self.assertEqual(list_buffer[5], "\033[37m \033[0m")
        self.assertEqual(list_buffer[6], "\033[32m \033[0m")
        self.assertEqual(list_buffer[7], "\033[34m \033[0m")
        self.assertEqual(list_buffer[8], "\033[33m \033[0m")
        self.assertEqual(list_buffer[9], "\033[31m \033[0m")

        self.assertEqual(list_buffer[10], "\033[40m \033[0m")
        self.assertEqual(list_buffer[11], "\033[47m \033[0m")
        self.assertEqual(list_buffer[12], "\033[42m \033[0m")
        self.assertEqual(list_buffer[13], "\033[44m \033[0m")
        self.assertEqual(list_buffer[14], "\033[43m \033[0m")
        self.assertEqual(list_buffer[15], "\033[41m \033[0m")

        self.assertEqual(list_buffer[16], "\033[30;40m \033[0m")
        self.assertEqual(list_buffer[17], "\033[37;47m \033[0m")
        self.assertEqual(list_buffer[18], "\033[32;42m \033[0m")
        self.assertEqual(list_buffer[19], "\033[34;44m \033[0m")
        self.assertEqual(list_buffer[20], "\033[33;43m \033[0m")
        self.assertEqual(list_buffer[21], "\033[31;41m \033[0m")

        self.assertEqual(list_buffer[22], "\033[1;30;40m \033[0m")
        self.assertEqual(list_buffer[23], "\033[3;30;40m \033[0m")
        self.assertEqual(list_buffer[24], "\033[4;30;40m \033[0m")

        self.assertEqual(list_buffer[25], "\033[1m ")
        self.assertEqual(list_buffer[26], "\n\x1b[0m")
        self.assertEqual(list_buffer[27], "\033[4m ")
        self.assertEqual(list_buffer[28], "\n\x1b[0m")
        self.assertEqual(list_buffer[29], "\033[3m ")
        self.assertEqual(list_buffer[30], "\n\x1b[0m")

    def test_cprint_fail(self):
        self.assertRaises(ColorUtilError, cprint, " ", cs=123)
        self.assertRaises(ColorUtilError, cprint, " ", all_line=1)

        self.assertRaises(CodeQueryError, cprint, " ", cs="123")






if __name__ == "__main__":
    unittest.main()