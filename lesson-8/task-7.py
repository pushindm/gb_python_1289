class ComplexNumber:
    def __init__(self, real, complex):
        self.real = real
        self.complex = complex
    
    def __str__(self):
        return f"{self.real}+{self.complex}j" if self.complex > 0 else f"{self.real}-{abs(self.complex)}j"
    
    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError("Second arg should be instance of 'ComplexNumber' class")
        return ComplexNumber(self.real+other.real, self.complex+other.complex)
    
    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError("Second arg should be instance of 'ComplexNumber' class")
        return ComplexNumber(self.real*other.real, self.complex*other.complex)
    
z1 = ComplexNumber(1,1)
z2 = ComplexNumber(-1,-1)
print(z1)
print(z1+z2)
print(z1*z2)