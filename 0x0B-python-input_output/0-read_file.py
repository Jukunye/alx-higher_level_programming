#!/usr/bin/python3
"""this module defines a function read_file"""


def read_file(filename=""):
    """reads a text file (utf-8) and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
