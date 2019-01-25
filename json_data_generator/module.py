#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan-11510 
# Date: 19/1/12
# version: 1.0
# python_version: 3.62

import json
import traceback
import xeger

"""
    get the modules list from the json object (dict in python)
    that is { dict => list }
    
    example json object
    {
        "modules":{
            "user": {
                "howMany": 500,
                "name":{
                    "template": "\\w{15,25}",
                    "unique": true
                },
                "password":{
                    "template": ".{5,30}",
                    "unique": false
                }
            },
            "movie": {
                "howMany": 20,
                "movie_id":{
                    "template": "\\d{4}",
                    "unique": true
                }
            }
        }
    }
    
    example output modules tuple
    (
        ("user",500,("name","\w{15,25}",true),("password",".{5,30}",false)),
        ("movie",20,("movie_id","\\d{4}",true))
    )
    
    @:param json_object : the input json object/dict
    @:return modules : the modules list
"""
def get_modules_tuple(json_object:dict):
    output_modules = []
    try:
        for module_tuple in dict(json_object.get("modules")).items():
            output_module = []

            # module_name
            output_module.append(module_tuple[0])

            for module_props_tuple in module_tuple[1].items():
                # module lines number
                if module_props_tuple[0] == "howMany":
                    output_module.append(module_props_tuple[1])
                # module props columns
                else:
                    output_module.append((module_props_tuple[0],module_props_tuple[1]["template"],module_props_tuple[1]["unique"]))
            # finish adding one module
            output_modules.append(tuple(output_module))
    except Exception:
        traceback.print_exc()
    return tuple(output_modules)



"""
    # from one configure list to generate one json data source
    
    example input modules list
        ["user",500,["name","\w{15,25}",true],["password",".{5,30}",false]]
    
    example output json source data
        user.json: 500 rows
        (
            "user",
            {"name": "aaaaaaaaaaaaaaaaaaaaaaa", "password": "abcdef"},
            {"name": "bbbbbbbbbbbbbbbbbbbbbbb", "password": "abcdef"}...
        )
"""
def json_data_generator(conf_tuple:tuple,max_length=50):
    try:
        output_file_name = conf_tuple[0]
        output_lines_numbers = conf_tuple[1]
        output_jsonlines = [output_file_name]

        props = conf_tuple[2:]

        generator = xeger.Xeger(max_length)

        # generate all needed mockup data
        output_temp_data = []
        # use the hash table to store and example whether repeat or not
        for prop in props:
            output_temp_one_col_data = ""
            if prop[2]:
                output_temp_one_col_data = {}
                for i in range(output_lines_numbers):
                    new_random = generator.xeger(prop[1])
                    while new_random in output_temp_one_col_data:
                        new_random = generator.xeger(prop[1])
                    output_temp_one_col_data[new_random] = True
                output_temp_data.append(list(output_temp_one_col_data.keys()))
            else:
                output_temp_one_col_data = []
                for i in range(output_lines_numbers):
                    output_temp_one_col_data.append(generator.xeger(prop[1]))
                output_temp_data.append(output_temp_one_col_data)

        for row in range(output_lines_numbers):
            one_line = {}
            for index,prop in enumerate(props):
                one_line[prop[0]] = output_temp_data[index][row]
            output_jsonlines.append(one_line)
        return output_jsonlines
    except Exception:
        traceback.print_exc()



# unit test
if __name__ == "__main__":
    file_path = "resource/module.json"

    modules = []
    with open(file_path,"r") as conf_file:
        conf_json_object = json.load(conf_file)

        modules = get_modules_tuple(conf_json_object)

    json_lines_data = json_data_generator(modules[0])

    for line in json_lines_data:
        print(line)
