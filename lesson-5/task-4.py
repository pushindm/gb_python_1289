# print user phrase using simple formating
from translate import Translator
translator = Translator(to_lang="ru")
translation = translator.translate("One")
with open(r"task-4\task-4.txt", encoding='utf-8') as input_file, open(r"task-4\task-4-translated.txt", 'w', encoding='utf-8') as output_file:
    separator = " — "
    for line in input_file:
        english_numeral, other_part = line.strip().split(separator)
        translation = translator.translate(english_numeral)
        print(translation + separator + other_part, file=output_file)
