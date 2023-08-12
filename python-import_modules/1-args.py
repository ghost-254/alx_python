#!/usr/bin/python3
import sys

def print_arguments(argv):
    num_arguments = len(argv)

    if num_arguments == 0:
        print("Number of argument(s): 0.")
        print(":")
        return
    
    if num_arguments == 1:
        print("Number of argument(s): 1.")
        print("1:", argv[0])
        return
    
    print("Number of argument(s):", num_arguments)
    print("Arguments:")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments(sys.argv[1:])
