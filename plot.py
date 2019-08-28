#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       : plot
@Author     : alanzhchou
@Create     : 19/8/28-22:53
@Python     : 3.62
@Version    : 1.0
@Email      : alanzhchou@gmail.com
@Copyright  : MIT License - Copyright (c) 2019 alanzhchou
@description:

@Change log :
19/8/28-22:53 created
"""
import matplotlib.pyplot as plt

single = {10: 0.01, 100: 0.005, 1000: 0.05}
muti_thread_single_connection = {
                                     10: {2: 0.001, 3: 0.05, 4: 0.06, 5: 0.005, 6: 0.15, 7: 0.006, 8: 0.1},
                                    100: {2: 0.002, 3: 0.08, 4: 0.05, 5: 0.003, 6: 0.18, 7: 0.016, 8: 0.08}
                                }


# single_key = list(single.keys())
# single_value = [ single[key] for key in single_key]
# print(single_key)
# print(single_value)
#
# plt.bar(range(len(single_value)), single_value, width=0.5, label='single', tick_label=single_key)
# plt.show()



# key_list = list(muti_thread_single_connection.keys())
#
# num_lists = [muti_thread_single_connection[key] for key in key_list]
#
# total_width, n = 2.4, len(num_lists)
# width = total_width / n
#
# x = list(range(len(num_lists[0])))
# print(x)
#
# for index in range(len(num_lists)):
#     plt.bar(x+index*width, num_lists[0], width=width, label='boy', tick_label=key_list, fc='y')
#
# plt.legend()
# plt.show()

