
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       : cut
@Author     : alanzhchou
@Create     : 19/8/28-22:51
@Python     : 3.62
@Version    : 1.0
@Email      : alanzhchou@gmail.com
@Copyright  : MIT License - Copyright (c) 2019 alanzhchou
@description:

@Change log :
19/8/28-22:51 created
"""
import matplotlib



def range_cut(counter: int, thread_number: int) -> list:
    result = []

    bottom = 1
    top = counter + 1

    step = int(counter / thread_number)

    for i in range(thread_number):
        result.append((bottom + i * step, bottom + (i+1) * step))

    print(result)



if __name__ == '__main__':
    range_cut(100000, 2)
    range_cut(100000, 3)
    range_cut(100000, 4)
    range_cut(100000, 5)
    range_cut(100000, 6)
    range_cut(100000, 7)
    range_cut(100000, 8)

