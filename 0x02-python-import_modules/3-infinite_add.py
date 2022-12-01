#!/usr/bin/python3
"""Prints the result of the addition of all arguments"""
if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv)
    total = 0
    for i in range(1, argv_len):
        total += int(argv[i])
    print(total)
