#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan-11510 
# Date: 19/1/12
# version: 1.0
# python_version: 3.62

import json
import xeger



# x = Xeger(25)
#
# for i in range(100):
#     print(x.xeger(".{15,18}"))
#     # print(x.xeger("^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"))


conf_path = "resource/module.json"

def read_from_json_conf(json_path):
    with open(json_path,"r") as f:
        conf = json.load(f)
        print(type(conf))
        print(conf)

read_from_json_conf(conf_path)