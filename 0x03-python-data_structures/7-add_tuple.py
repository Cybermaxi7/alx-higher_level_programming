#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    new_tup1 = tuple_a + (0, 0)
    new_tup2 = tuple_b + (0, 0)
    new_tuple = new_tup1[0] + new_tup2[0], new_tup1[1] + new_tup2[1]
    return new_tuple
