#!/usr/bin/python3
""" replaces or adds key/value in a dictionary """


def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary.copy()
    new_dict.update({key: value})
    return new_dict
