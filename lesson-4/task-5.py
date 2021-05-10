# Calculate cumulative product of all even numbers from a given range
from functools import reduce

def number_product(val1, val2):
    return val1 * val2


left_margin = 100
right_margin = 1000
sample_list = [i for i in range(left_margin, right_margin+1) if i % 2 == 0]
cumulative_sum = reduce(number_product, sample_list)
print(f"The cumulative product of all even numbers from the range [{left_margin}, {right_margin}] is {cumulative_sum}")
