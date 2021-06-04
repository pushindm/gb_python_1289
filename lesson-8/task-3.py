class ListTypeError(Exception):
    pass

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
user_list = []
curr_el = ''
while curr_el != 'stop':
    try:
        curr_el = input("Enter number or enter 'stop' for exit: ")
        if not is_number(curr_el.lstrip('-')):
            raise ListTypeError
    except ListTypeError:
        print("Incorrect element type. Please, enter a number")
    else:
        user_list.append(curr_el)

print(user_list)
