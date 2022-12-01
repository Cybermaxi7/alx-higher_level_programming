#!/usr/bin/python
"""
Simple program that import add function.
And print the sum result of two variables
"""
from add_0 import add
a = 1
b = 2

if __name__ == "__main__":
	print("{:d} + {:d} = {:d}".format(a,b,add(a,b)))
