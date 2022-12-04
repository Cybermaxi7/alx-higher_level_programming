#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    reversed_lists = reversed(my_list)
    for val in reversed_lists:
        print("{:d}".format(val))
