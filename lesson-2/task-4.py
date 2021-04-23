# print user phrase using simple formating
def phrase_print(my_list):
    threshold = 10
    for pos, word in enumerate(my_list):
        if len(word) > threshold:
            word = word[:threshold]
        print(f"{pos+1}: {word}")


# main
user_list = input("Enter your phrase: ").split()
phrase_print(user_list)
