# A program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

if __name__ == "__main__":
    a = 1
    b = 2

    exec(open("add_0.py").read())

    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
