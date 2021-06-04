import math

class Cell:
    def __init__(self, cellNumber):
        self.cellNumber = cellNumber
    
    @property
    def cellNumber(self):
        return self._cellNumber
    
    @cellNumber.setter
    def cellNumber(self, value):
        if value < 0:
            raise ValueError("The number of cells can not be negative")
        self._cellNumber = math.floor(value)
        
    def __add__(self, other):
        if not isinstance(other, Cell):
            raise ValueError("The second arg should be a member of class Cell")
        return Cell(self.cellNumber + other.cellNumber)
    
    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise ValueError("The second arg should be a member of class Cell")
        if (self.cellNumber - other.cellNumber) > 0:
            return Cell(self.cellNumber - other.cellNumber)
        else:
            print("The result of substraction is not positive. Zero value was returned")
            return 0
    
    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise ValueError("The second arg should be a member of class Cell")
        return Cell(self.cellNumber*other.cellNumber)
    
    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise ValueError("The second arg should be a member of class Cell")
        return Cell(self.cellNumber // other.cellNumber) if bool(other.cellNumber) else None
    
    def __str__(self):
        return f"Current cell number: {self.cellNumber}"
    
    def make_order(self, cells_in_row):
        output_list = []
        for i in range(1, self.cellNumber+1):
            if i != self.cellNumber:
                output_list.append("*\n" if i % cells_in_row == 0 else '*')
            else:
                output_list.append('*') # exclude last line break
        return ''.join(output_list)
    
# main
A = Cell(12)
B = Cell(3)
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A.make_order(5))
