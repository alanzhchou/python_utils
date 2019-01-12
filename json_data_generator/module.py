#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan-11510 
# Date: 19/1/12
# version: 1.0
# python_version: 3.62

import json

"""
    get the modules list from the json object (dict in python)
    that is { dict => list }
    
    example json object
    {
        "modules":{
            "user": {
                "howMany": 500,
                "name":{
                    "template": "\w{15,25}",
                    "unique": true
                },
                "password":{
                    "template": ".{5,30}",
                    "unique": false
                }
            }
        }
    }
    
    example output modules list
    [
        ["user",500,],
    ]
    
    @:param json_object : the input json object/dict
    @:return modules : the modules list
"""
def get_modules_list(json_object:dict):
    modules = []
    if not isinstance(json_object,dict):
        raise ValueError("not a dict (json object in python)")
    try:
        print(json_object)
        # modules_object =
    except Exception:
        print("error")

    return []










# class test
if __name__ == "__main__":
    file_path = "resource/module.json"

    with open(file_path,"r") as conf_file:
        conf_json_object = json.load(conf_file)

        get_modules_list(conf_json_object)

