#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dictionary = sorted(a_dictionary)
    for i in sort_dictionary:
        print("{}: {}".format(i, a_dictionary.get(i)))
