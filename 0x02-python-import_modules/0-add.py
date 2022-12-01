#!/usr/bin/python3
"""
A program that import add function
and print sum result of two variables
"""

if __name__ == "__main__":
    from add-0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
