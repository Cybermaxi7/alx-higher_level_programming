#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if my_string == None:
        return
    for char in my_string:
        if char != 'C' and char != 'c':
            new_string += char
    return new_string
