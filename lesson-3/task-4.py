def negative_power(val, power):
    """Find the negative whole power of a positive real number"""
    try:
        val, power = float(val), float(power)
        if val > 0 and power.is_integer() and power < 0:
            ans = val
            power = abs(power)
            while power - 1 != 0:
                ans *= val
                power -= 1
            return 1 / ans
        else:
            print("Your input was incorrect. Please, rerun the program with the right numbers type")
    except ValueError:
        print("Oops. Some of your values are not numbers.")


# main
user_value = input("Enter positive real number: ")
user_power = input("Enter a power (negative whole number): ")
answer = negative_power(user_value, user_power)
if answer != None:
    print(f"The number {user_value} to the power of {user_power} is equal to {answer:.3f}")
