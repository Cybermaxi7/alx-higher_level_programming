#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_lists = reversed(my_list)
    for val in reversed_lists:
        print("{:d}".format(val))
