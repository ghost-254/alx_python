# A program that prints numbers from 0 to 99 in 2 digits.
for a in range(0, 100):
    print("{:02d}".format(a), end=", " if a < 99 else "\n")
