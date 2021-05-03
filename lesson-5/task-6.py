with open(r"task-6\task-6.txt", encoding='utf-8') as f:
    my_dict = {}
    for line in f:
        discipline_name, other_part = line.strip().split(': ')
        value_string = other_part.replace('(л)', '').replace('(пр)', '').replace('(лаб)', '')
        value_list = map(float, value_string.split())
        my_dict[discipline_name] = sum(value_list)
    print(my_dict)
