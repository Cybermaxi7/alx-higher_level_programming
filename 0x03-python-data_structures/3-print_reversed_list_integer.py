#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_lists = reversed(sorted(my_list))
    for val in reversed_lists:
        print("{:d}".fornat(val))
