# Salary calculation
from sys import argv

def salary_calculation(val_list):
    try:
        hours, hourly_rate, bonus = [float(el) for el in val_list]
        salary = (hours * hourly_rate) * (1 + bonus)
        print(f"Month salary: {salary:.2f}")
    except ValueError:
        print("Oops. Please, use three float numbers")


# main
salary_calculation(argv[1:])
