#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan Chou 
# Date: 19/6/13
# version: 1.0
# python_version: 3.62

# MIT License
# Copyright (c) 2019 alanzhchou
# email: alanzhchou@gmail.com


import sys

class Stream():
    @staticmethod
    def set_ignore(s):
        pass

    @staticmethod
    def write(s):
        pass

    @staticmethod
    def get():
        pass

    @staticmethod
    def clear():
        pass



class ListStream(Stream):
    _data = []
    _ignore_string = ""

    @staticmethod
    def set_ignore(ignore_string:str):
        ListStream._ignore_string = ignore_string

    @staticmethod
    def write(s):
        '''
        write to _data list, ignore given ignore string, can not append ignore string
        such
            list_stream = redirect_stdout_to(ListStream, ignore="\n")
            print("123")
            print("\n")
            list_stream will remain only "123", that is len(list_stream.get()) = 1
        :param s: string need redirect to this List_stream
        '''
        if s != ListStream._ignore_string:
            ListStream._data.append(s)

    @staticmethod
    def get() -> list:
        return ListStream._data

    @staticmethod
    def clear():
        ListStream._data.clear()



def redirect_stdout_to(stream_type:type, ignore:str = "") -> Stream:
    sys.stdout = stream_object = stream_type()
    stream_object.set_ignore(ignore)
    return stream_object

def clear_stdout_redirect():
    sys.stdout = sys.__stdout__



def redirect_stderr_to(stream_type : type) -> Stream:
    sys.stderr = stream_object = stream_type()
    return stream_object

def clear_stderr_redirect():
    sys.stdout = sys.__stderr__



if __name__ == "__main__":
    from colprint.cprint import cprint

    list_stream = redirect_stdout_to(ListStream, ignore="\n")

    cprint(" ", cs="+")
    cprint(" ", cs="_")
    print("123")
    cprint(" ", cs="+", all_line=True)

    clear_stdout_redirect()

    list_buffer = list_stream.get()

    assert "\033[1m \033[0m" == list_buffer[0]
    assert "\033[4m \033[0m" == list_buffer[1]
    # print(list_buffer)
    assert len(list_buffer) == 5

    # print(str(list_buffer[3]).encode())
    list_stream.clear()