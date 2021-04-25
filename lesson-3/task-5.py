def simple_summator(user_vals):
    """Sum any float numbers inputed by a user"""
    try:
        user_numbers = list(map(float, user_vals))
        return sum(user_numbers)
    except ValueError:
        print("Oops. Some of your values are not real numbers.")
        # raise


# main
end_symbol = ''
current_sum = 0
total_sum = 0

while end_symbol != "\\":
    user_values_list = input("Enter numbers or backslash symbol for quit: ").split()
    end_symbol = user_values_list[-1]
    current_sum = simple_summator(user_values_list) if end_symbol != "\\" else simple_summator(user_values_list[:-1])
    if current_sum is not None:
        total_sum += current_sum
        print(f"Total_sum: {total_sum}")
