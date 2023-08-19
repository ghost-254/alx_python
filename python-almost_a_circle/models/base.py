#!/usr/bin/python3
"""
base.py
A module that manages id attributes in all the future classes and to avoid duplicating the same code (by extension, same bugs)
"""
class Base:
    """
    Base class for managing id attribute across all classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base instance.

        Args:
            id (int): The unique identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
