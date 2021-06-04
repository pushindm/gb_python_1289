class Storage:
    pass

class OfficeEquipment:
    
    def __init__(self, name, price, amount=1):
        self.name = name
        self.price = price
        self.amount = amount
    
    def __str__(self):
        return 'Type: {0.__class__.__name__}, model: {0.name}, price: {0.price}, amount: {0.amount}'.format(self)
    
class Printer(OfficeEquipment):
    def __init__(self, name, price, amount, printer_type):
        OfficeEquipment.__init__(self, name, price, amount)
        self.printer_type = printer_type
            
    def __str__(self):
        return '{0}, printer_type: {1.printer_type}'.format(super().__str__(), self)

class Scaner(OfficeEquipment):
    def __init__(self, name, price, amount, dim):
        OfficeEquipment.__init__(self, name, price, amount)
        self.dim = dim 
    
    def __str__(self):
        return '{0}, dim of scanning: {1.dim}'.format(super().__str__(), self)

class Xerox(OfficeEquipment):
    def __init__(self, name, price, amount, is_portable):
        OfficeEquipment.__init__(self, name, price, amount)
        self.is_portable = is_portable
    
    def __str__(self):
        return '{0}, portability: {1}'.format(super().__str__(), bool(self.is_portable))

printer = Printer('hp', 3, 3, 'color')
print(printer.price)

scaner = Scaner('canon', 2, 5, '1D')
print(scaner)

xerox = Xerox('dell', 10, 10, 0)
print(xerox)