# example of generator using
def my_func(vals_list):
    filtered_vals_list = [vals_list[i+1] for i in range(len(vals_list)-1) if vals_list[i+1] > vals_list[i]]
    print(f"New list: {filtered_vals_list}")


# main
test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Sample list: {test_list}")
my_func(test_list)
