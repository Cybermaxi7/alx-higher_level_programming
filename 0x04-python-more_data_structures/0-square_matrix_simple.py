#!/usr/bin/python3
""" return the square value of 2-dimensional list """


def square_matrix_simple(matrix=[]):
    if matrix:
        return [list(map(lambda x: x * x, vals)) for vals in matrix]
