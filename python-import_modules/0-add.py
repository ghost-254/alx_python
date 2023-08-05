# A program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
from add_0 import add

def main():
    a = 1
    b = 2
    result = add(a, b)
    print(f"{a} + {b} = {result}")

if __name__ == "__main__":
    main()
