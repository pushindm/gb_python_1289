# print user data in one line
def print_user_data(**kwargs):
    vals_list = list(kwargs.values())
    vals_string = ' '.join(vals_list)
    print(f"Your input: {vals_string}")


# main
graph_names_list = ["first name", "second name", "birth year", 
                    "residence city", "email", "mobile"]
counter = 0
user_data = []

print("Enter some info about you.")
while counter != len(graph_names_list):
    new_data = input(graph_names_list[counter] + ": ")
    user_data.append(new_data)
    counter += 1

print_user_data(first_name=user_data[0], second_name=user_data[1], birth_year=user_data[2], 
                residence_city=user_data[3], email=user_data[4], mobile=user_data[5])
