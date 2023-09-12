#!/usr/bin/python3
"""this module defines a function that appends text"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
