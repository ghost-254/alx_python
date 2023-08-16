#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size
    
    def get_size(self):
        return self.__size
    
    def set_size(self, new_size):
        if new_size >= 0:
            self.__size = new_size
        else:
            raise ValueError("Size cannot be negative")
    
    def __str__(self):
        return f"Square with side length {self.__size}"
