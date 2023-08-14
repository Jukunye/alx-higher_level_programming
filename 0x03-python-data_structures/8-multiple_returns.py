#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with the length of a string and its first character"""
    length = len(sentence)
    if length == 0:
        result = (length, None)
    else:
        result = (length, sentence[0])

    return (result)
