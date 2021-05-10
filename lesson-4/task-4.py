def find_unique_values(vals_list):
    """Find unique list values"""
    unique_vals_list = [el for el in vals_list if vals_list.count(el) == 1]
    return unique_vals_list


# main
sample_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"Sample list: {sample_list}")
unique_values = find_unique_values(sample_list)
print(f"Unique values: {unique_values}")
