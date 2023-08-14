#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """function that replaces an element without modifying the original"""
    if idx < 0 or idx >= len(my_list):
        return (my_list[:])
    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
