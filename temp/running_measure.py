#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File     : log_func_time
@Author   : 周恒-z50003220
@Email    : zhouheng18@huawei.com
@Create   : 2019/8/13-11:38
@Python   ：Python 3.7.3
@IDE      : PyCharm
@Version  : 0.0.1

@Change_log
2019/8/13-11:38 created
"""
import sys
import time
import traceback
from inspect import getmodule
from functools import wraps
from types import ModuleType, FunctionType

import psutil
from gc import get_referents


def log_run_time_second_print(func: FunctionType):
    """
    decorator for printing some functions running time, in second
    format such as
        2.50001 seconds run for < [function] my_function_name > defined in < [module] mu_module_path >
    :param func:
    :return:
    """
    @wraps(func)
    def method_run_proxy(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        module_file = getmodule(func).__file__
        print(f'\n{end - start} seconds run for <[function] {func.__name__}> defined in <[module] {module_file}>')
        return result
    return method_run_proxy


def log_run_time_second_return(func: FunctionType):
    """
    decorator for calculating some functions running time, in second
    different with < log_run_time_second_print > defined in this module,
    this decorator return running time first then function result
    return such as
        2.50001, my_function_result
    :param func:
    :return: running_time in second
            running_result
    """
    @wraps(func)
    def method_run_proxy(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return end - start, result
    return method_run_proxy


def log_start_end_cpu_and_mem_print(func: FunctionType):
    """
    using psutil
    decorator for calculating some functions running cpu and memory use,
    print these infomation at the end of target function
    :param func:
    :return:
    """
    @wraps(func)
    def method_run_proxy(*args, **kwargs):
        # 初始时cpu使用率
        start_cpu = psutil.cpu_percent()
        # 初始时内存使用率
        start_mem = psutil.virtual_memory().percent

        result = func(*args, **kwargs)

        # 初始时cpu使用率
        end_cpu = psutil.cpu_percent()
        # 初始时内存使用率
        end_mem = psutil.virtual_memory().percent

        module_file = getmodule(func).__file__
        print(f'\nstart_cpu: {start_cpu}, start_mem: {start_mem}')
        print(f'end_cpu: {end_cpu}, end_mem: {end_mem}')
        print(f'run for <[function] {func.__name__}> defined in <[module] {module_file}>')
        return result
    return method_run_proxy


def log_start_end_cpu_and_mem_return(func: FunctionType):
    """
    using psutil
    decorator for calculating some functions running cpu and memory use
    return these infomation at the end of target function
    return such as
        start_cpu, start_mem, end_cpu, end_mem, my_function_result
    :param func:
    :return: start_cpu
            start_mem
            end_cpu
            end_mem
            my_function_result
    """
    @wraps(func)
    def method_run_proxy(*args, **kwargs):
        # 初始时cpu使用率
        start_cpu = psutil.cpu_percent()
        # 初始时内存使用率
        start_mem = psutil.virtual_memory().percent

        result = func(*args, **kwargs)

        # 初始时cpu使用率
        end_cpu = psutil.cpu_percent()
        # 初始时内存使用率
        end_mem = psutil.virtual_memory().percent

        return start_cpu, start_mem, end_cpu, end_mem, result
    return method_run_proxy


def try_except_with_debug(debug: bool = True):
    def try_except_with_debug_achieve_decorator(func: FunctionType):
        @wraps(func)
        def method_run_proxy(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if debug:
                    traceback.print_exc()
                    module_file = getmodule(func).__file__
                    print(f'\n\033[1;31m => exception for <[function] {func.__name__}> defined in <[module] {module_file}>\033[m')
                else:
                    pass
        return method_run_proxy
    return try_except_with_debug_achieve_decorator


def get_obj_size_bytes(obj: object) -> int:
    """
    sum size of object & members. size scale in bytes
    """
    # Custom objects know their class.
    # Function objects seem to know way too much, including modules.
    # Exclude modules as well.
    BLACKLIST = type, ModuleType, FunctionType
    if isinstance(obj, BLACKLIST):
        raise TypeError('get_obj_size() does not take argument of type: '+ str(type(obj)))

    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size


if __name__ == '__main__':
    # import redis
    # from util.lazy_init import lazy_init_context
    # lazy_init_context()
    # from softcomai.sdk.api.redis.handler import RedisAloneClient
    #
    # redis_connection_1 = RedisAloneClient.create_redis_conn(host='127.0.0.1', port=6379, password='@@Changeme_123')
    # redis_connection_2 = RedisAloneClient.create_redis_conn(host='127.0.0.1', port=6379, password='@@Changeme_123')
    # redis_connection_3 = redis.Redis(connection_pool=redis_connection_1.connection_pool)
    #
    # print(id(redis_connection_1.connection_pool))
    # print(id(redis_connection_2.connection_pool))
    # print(id(redis_connection_3.connection_pool))

    @try_except_with_debug(debug=True)
    def one():
        raise Exception
    one()

