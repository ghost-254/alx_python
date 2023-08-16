#!/usr/bin/python3
"""
2-inherits_from.py
A module that provides the inherits_from function for checking class inheritance.
"""
def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited from the specified class;
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
