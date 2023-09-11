#!/usr/bin/python3
"""
This module inherits list class
"""


class MyList(list):
    """
    Mylist inherists list
    """
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
