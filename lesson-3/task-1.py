# find quotient of two numbers with handling of simple exceptions
def find_quotient(a, b):
    try:
        ans = float(a) / float(b)
        print(f"The quotient of {a} by {b} is equal to {ans:.3f}")
        return ans
    except (ZeroDivisionError, ValueError) as e:
        print("Oops. Please, enter two non-zero float numbers. Current error:", e)


a, b = input("Enter dividend and divisor: ").split()
quotient = find_quotient(a, b)
