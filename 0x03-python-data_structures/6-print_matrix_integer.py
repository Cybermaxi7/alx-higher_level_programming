#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        for idx, val in enumerate(row):
            print("{:d}".format(val), end=" " if idx < len(row) - 1 else "")
        print()
