# determine the season by the month value
def which_season(m, flag):
    if int(flag):
        base_list = ('Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer','Autumn', 'Autumn', 'Autumn', 'Winter')
        for i in range(len(base_list)):
            if i == int(m)-1:
                print(f"The {m} month is a {base_list[i]}")
    else:
        base_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer',
                     7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
        print(f"The {m} month is a {base_dict.get(int(m))}")

# main
user_month = input("Enter a month name as an integer number: ")
program_realization = input("Which program realization should be used? Type 0 (via dict) or 1 (via list): ")
which_season(user_month, program_realization)
