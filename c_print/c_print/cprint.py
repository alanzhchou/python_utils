#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Author: Alan Chou 
# Date: 19/6/11
# version: 1.0
# python_version: 3.62

# MIT License
# Copyright (c) 2019 alanzhchou
# email: alanzhchou@gmail.com


'''
from "http://ozzmaker.com/add-colour-to-text-in-python/"

Text color 	Code 	Text style 	Code 	Background color 	Code
Black 	    30 	    No effect 	0 	    Black 	40
Red 	    31 	    Bold 	    1 	    Red 	41
Green 	    32 	    Underline 	2 	    Green 	42
Yellow 	    33 	    Negative1 	3 	    Yellow 	43
Blue 	    34 	    Negative2 	5 	    Blue 	44
Purple 	    35 			                Purple 	45
Cyan 	    36 			                Cyan 	46
White 	    37 			                White 	47

full parameter =>
print("\033[1;32;40m Bright Green  \n")

\033[  Escape code, this is always the same
1 = Style, 1 for normal.
32 = Text color, 32 for bright green.
40m = Background color, 40 is for black.


only set the text color
print("\033[31m RED \n")

31 = Text color, 31 for red
m = background color, default not set
'''


import os

class ColorUtilError(Exception):
    pass

class CodeQueryError(ColorUtilError):
    pass


class ColorAndStyle():
    '''
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
    '''
    ESCAPE_CODE_PREFIX = "\033["
    INITIAL_CODE = "\033[0m"

    # front text color
    F_DARK = "30"
    F_WHITE = "37"
    F_GREEN = "32"
    F_ORANGE = "33"
    F_BLUE = "34"
    F_RED = "31"

    # background color
    B_DARK = "40"
    B_WHITE = "47"
    B_GREEN = "42"
    B_ORANGE = "43"
    B_BLUE = "44"
    B_RED = "41"

    # font style
    STYLE_UNDERLINE = "4"
    STYLE_ITALIC = "3"
    STYLE_BOLD = "1"

    MAN_QUERY_DICT = {
        "_" : STYLE_UNDERLINE,
        "/" : STYLE_ITALIC,
        "+" : STYLE_BOLD,

        "d": F_DARK,
        "w": F_WHITE,
        "g": F_GREEN,
        "o": F_ORANGE,
        "b": F_BLUE,
        "r": F_RED,

        "D": B_DARK,
        "W": B_WHITE,
        "G": B_GREEN,
        "O": B_ORANGE,
        "B": B_BLUE,
        "R": B_RED
    }

    @staticmethod
    def _get_single_code(code:str) -> str:
        '''
        query ansi code from definded 'MAN_QUERY_DICT'
        :param code: one man used color or style code(one char)
        :return: one ansi code
        :raise: CodeQueryError if not exist in 'MAN_QUERY_DICT'
        '''
        if code in ColorAndStyle.MAN_QUERY_DICT:
            return ColorAndStyle.MAN_QUERY_DICT.get(code)
        raise CodeQueryError("error input code, support for '+/_' and 'dDwWgGoObBrR'")

    @staticmethod
    def _get_ANSI_color_and_style_code(c_and_s: str) -> str:
        '''
        get ansi color code form man recognition string
        :param c_and_s: man recognition string => in 3 chars string
                example as '+gB'
        :return: ansi color code with escape code
                example as '\033[1;32;40m'
        :raise: CodeQueryError if not exist in 'MAN_QUERY_DICT'
        '''
        if len(c_and_s) > 3:
            c_and_s = c_and_s[:3]

        ansi_codes = ColorAndStyle.ESCAPE_CODE_PREFIX

        code_list = []
        for code in c_and_s:
            try:
                code_list.append(ColorAndStyle._get_single_code(code))
            except Exception as e:
                raise e
        return ansi_codes + ";".join(code_list) + "m"


'''
export 1 public functions
:raise CodeQueryError => ("error input code, support for '+/_' and 'dDwWgGoObBrR'")
:raise ColorUtilError => ("wrong code type, must be str or sub class")
'''
os.system('COLOR 07')

def cprint(*args, cs:str="", all_line:bool=False, sep:str=' ', end:str='\n'):
    '''
    print to console with given color and style codes (immediately reset to initial color mode)
    :param cs: the color and style code
    :param args: string args
    :param sep: sepeator
    :param end: string end
    :raise ColorUtilError if codes is not str or sub class => ("wrong code type, must be str or sub class")
    '''
    if isinstance(cs, str) and isinstance(all_line, bool):
        if sep.join(str(arg) for arg in args) != "":
            try:
                color_and_style_perfix = ColorAndStyle._get_ANSI_color_and_style_code(cs)
            except Exception as e:
                raise e

            c_and_s_output = color_and_style_perfix + sep.join(str(arg) for arg in args)
            if not all_line:
                print(c_and_s_output + ColorAndStyle.INITIAL_CODE, end=end)
            else:
                print(c_and_s_output, end="\n" + ColorAndStyle.INITIAL_CODE)
        else:
            if not all_line:
                print(*args, sep=sep, end=end)
            else:
                print(*args, sep=sep, end="\n")
    else:
        raise ColorUtilError("wrong code type, cs must be str or sub class, all_line must be bool")





if __name__ == "__main__":
    debug = True
    if debug:
        cprint("123",cs="_bW")
        cprint(1,2,3,cs="_bW")
        cprint("", cs="_bW")
        print("normally")

        cprint("*******************************************",cs="+gW")

        cprint("123",cs="_bW",end="")
        cprint(1,2,3,cs="_bW",end="")
        cprint("", cs="_bW",end="")
        print("normally")

        cprint("*******************************************",cs="+gW")

        cprint("","",cs="_bW")
        print("normally")

        cprint("*******************************************",cs="+gW")

        cprint("123",cs="_bW",all_line=True)
        cprint(1,2,3,cs="_bW",all_line=True)
        cprint("", cs="_bW",all_line=True)
        print("normally")

        cprint("*******************************************",cs="+gW")

        cprint("","",cs="_bW",all_line=True)
        print("normally")
        cprint(" ",cs="_bW",all_line=True)


