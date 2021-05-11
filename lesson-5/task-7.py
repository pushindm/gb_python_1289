import json

with open(r"task-7\task-7.txt", encoding='utf-8') as input_file, open(r"task-7\task-7.json", 'w') as output_file:
    name_list = []
    profit_list = []
    for line in input_file:
        name, own_type, revenue, loss = line.strip().split()
        name_list.append(name)
        profit_list.append(float(revenue) - float(loss))
    temp_list = [profit for profit in profit_list if profit > 0]
    average_profit = {"average_profit": sum(temp_list) / len(temp_list)}
    firm_dict = dict(zip(name_list, profit_list))
    output_list = [firm_dict, average_profit]
    json.dump(output_list, output_file)
