#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2

    exec(open("add_0.py").read())

    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
