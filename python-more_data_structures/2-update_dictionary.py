#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())
    for key in keys:
        print(f"{key}: {a_dictionary[key]}")
