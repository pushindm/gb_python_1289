def string_capitalizer(word_list):
    """
    Return the string where every word begins with a capital letter. The input is a list of words.
    
    >>> string_capitalizer(['hello','world'])
    'Hello World'
    """
    def int_func(word):
        return word.title()
    
    modified_word_list = []
    for word in word_list:
        if word[0].isalpha() and not word.istitle():
            modified_word_list.append(int_func(word))
        else:
            modified_word_list.append(word)
    output_string = ' '.join(modified_word_list)
    return output_string


# main
output_string = string_capitalizer(input("Enter your string: ").split())
print(f"Output: {output_string}")
