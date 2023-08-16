#!/usr/bin/python3
"""
1-is_kind_of_class.py
A module that provides the is_kind_of_class function for checking object class hierarchy.
"""
def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it's an instance of a class that inherited from,
    the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or its subclasses; otherwise False.
    """
    return isinstance(obj, a_class)
