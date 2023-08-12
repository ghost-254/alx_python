#!/usr/bin/python3
def raise_exception():
    value = "string"
    try:
        # We then attempt to treat value as an integer
        result = value + 1
    except TypeError:
        print("Exception has been raised")
