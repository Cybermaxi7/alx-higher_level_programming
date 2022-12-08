#!/usr/bin/python3
""" return the sum of unique int in a list """


def uniq_add(my_list=[]):
    new_list = set(my_list)
    return sum(new_list)
