def my_func(val_1, val_2, val_3):
    """Calc the sum of the two largest numbers out of three numbers entered by a user."""
    try:
        val_1, val_2, val_3 = float(val_1), float(val_2), float(val_3)
        vals_list = [val_1, val_2, val_3]
        unique_vals_list = list(set(vals_list))
        min_val = min(unique_vals_list)
        vals_list.remove(min_val)
        answer = sum(vals_list)
        print(f"The sum of the two highest numbers is equal to {answer}")
    except ValueError:
        print("Oops. Some of your values are not real numbers.")


# main
a, b, c = input("Enter your values: ").split()
my_func(a, b, c)
