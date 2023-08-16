#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    return [[column ** 2 for column in row] for row in matrix]
