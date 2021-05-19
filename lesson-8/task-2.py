class ZeroDivisionError(Exception):
    pass

def simple_division(a, b):
    try:
        a, b = float(a), float(b)
        if b == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print('Division by zero is not allowed')
    except ValueError as e:
        print(str(e))
    else:
        return a / b

a, b = input("Enter two numbers separated by space: ").split()
ans = simple_division(a, b)
if ans:
    print(ans)