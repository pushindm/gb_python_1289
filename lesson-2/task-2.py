# simple permutation of list elements
def simple_permutation(ls):
    for i in range(0, len(ls) - 1, 2):
       (ls[i], ls[i+1]) = (ls[i+1], ls[i])
    return ls


# main
user_list = (input("Enter list values: ").split())
print(simple_permutation(user_list))
