# create a file with data
with open(r"task-1\task-1.txt", 'w') as f:
    while True:
        user_line = input("Enter a data for writing or empty line for exit: ")
        if user_line:
            print(user_line, file=f)
        else:
            break
