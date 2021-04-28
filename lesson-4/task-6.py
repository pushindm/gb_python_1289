# example of itertools possibilities
from itertools import count, cycle

# create and print powers of two
for el in count(1):
    if el < 5:
        print(el)
    else:
        print('Finish first cycle')
        break

sample_list = ['1', '2', '3']
total_sum = 0
for el in cycle(sample_list):
    total_sum += int(el)
    print(f"Current el: {el}. Current sum: {total_sum}")
    if total_sum > 10:
        break
