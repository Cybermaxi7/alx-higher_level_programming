#!/usr/bin/python
"""
Simple program that import add function.
And print the sum result of two variables
"""
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
