#!/usr/bin/bash
""" Script return's an element based on a given index value"""


def element_at(my_list, idx):
    if idx <= -1:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
