#!/usr/bin/python3
""" returns a new dictionary with all values multiplied by 2 """


def multiply_by_2(a_dictionary):
    new_dict = dict((k, v*2) for k, v in a_dictionary.items())
    return new_dict
