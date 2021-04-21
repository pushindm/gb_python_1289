# simple products database
def data_loading(p, p_list, index):
    keys = ("название", "цена", "количество", "ед")
    for i in range(1,3):
        p[i] = int(p[i])
    el = dict(zip(keys, p))
    p_list.append((index, el))

# main
new_product_name = ''
products_list = []
counter = 0
while new_product_name != 'quit':
    new_product = input("Enter info about a new good (format: name price amount units) or enter 'quit' to finish: ").split()
    new_product_name = new_product[0]
    if new_product_name != 'quit':
        counter += 1
        data_loading(new_product, products_list, counter)

# output of user inputs
print("Your products:")
for p in products_list:
    print(p)
