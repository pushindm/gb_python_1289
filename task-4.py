# find max digit in a number
def max_digit(n):
    i = 0
    max_val = int(n[0])
    while i < len(n):
        curr_digit = int(n[i])
        if max_val < curr_digit:
            max_val = curr_digit
        i += 1
    print(f"The greatest digit in {int(n)} is {max_val}")


# main
max_digit(input("Type int number: "))
