sample_list = ['1', '2', '3', '4']
with open(r"task-5\task-5.txt", 'w') as f:
    f.write(' '.join(sample_list))

with open(r"task-5\task-5.txt") as f:
    number_string = f.readline().strip()
    number_list = [float(num) for num in number_string.split()]
    print(f"Sum: {sum(number_list)}")
