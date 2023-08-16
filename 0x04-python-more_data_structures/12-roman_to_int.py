#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a Roman numeral to an integer"""
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    result = 0

    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in reversed(roman_string):
        val = romans[i]
        result += val if result < val * 5 else -val
        return result
