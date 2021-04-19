# get and print user info
user_first_name = "first_name"
user_mail = "e-mail"
user_age = "age"
print(f'''Please, input your first name, email and age in a format: {user_first_name} {user_mail} {user_age}''')

# user data
user_first_name, user_mail, user_age = input("Your data: ").split(' ')
user_age = int(user_age)
print(f'''Your input: {user_first_name} {user_mail} {str(user_age)}''')
