#!/usr/bin/python3
"""this module defines a json file-reading function"""
import json


def load_from_json_file(filename):
    """Creates a python object from a given json file"""
    with open(filename, 'r') as f:
        return json.load(f)
