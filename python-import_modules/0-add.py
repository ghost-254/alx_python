# A program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
exec(open("add_0.py").read())

def main():
    a = 1
    b = 2
    result = (a + b)
    print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    main()
