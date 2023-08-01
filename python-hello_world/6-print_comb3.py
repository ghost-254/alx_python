# Printing all possible combinations of numbers with two digits
for tens_digit in range(0, 10):
    for ones_digit in range(tens_digit + 1, 10):
        print("{:02d}".format(tens_digit * 10 + ones_digit), end=", " if ones_digit < 9 else "\n")
