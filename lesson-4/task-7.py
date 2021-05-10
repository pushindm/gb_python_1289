def fact(n):
    index = 1
    current_factorial = 1
    while index <= n:
        yield current_factorial
        index += 1
        current_factorial *= index

for el in fact(4):
    print(el)
