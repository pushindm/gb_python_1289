class WrongFormatError(Exception):
    pass

class WrongDate(Exception):
    pass

class Data:
    # class atr
    data_string = ''
    
    def __init__(self, user_str):
        Data.data_string = user_str
    
    @classmethod
    def on_get_data(cls):
        try:
            if cls.data_string.count('-') != 2:
                raise WrongFormatError
        except WrongFormatError:
            print("Incorrect format type. Use the following date format 'dd-mm-yy': ")
        except ValueError as e:
            print(str(e))
        else:
            return [int(el) for el in cls.data_string.split('-') if el.isnumeric()]
    
    @staticmethod
    def data_validator(ls):
        try:
            d, m, y = ls
            if not (1<=d<=31 and 1<=m<=12 and 1900<=y):
                raise WrongDate
        except WrongDate:
            print("Check date format. Use the following date format 'dd-mm-yy'")
        else:
            print('Date is OK')


Data.data_string = input("Input date in the format: dd-mm-year: ")
# convert data in list of ints
test_list = Data.on_get_data()
# check if data correct
if test_list:
    Data.data_validator(test_list)
