# example of generator using
new_list = [i for i in range(20, 241, 1) if i % 20 == 0 or i % 21 == 0]
print(f"{new_list}")
