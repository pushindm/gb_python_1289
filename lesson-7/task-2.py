from abc import ABC, abstractmethod

class ClothesAbstractClass(ABC):
    """Abstract class for calculation amount of cloth for different type of clothes"""
    @abstractmethod
    def cloth_amount_calculation(self):
        pass

class Clothes(ClothesAbstractClass):
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("The cloth amount should be great than 0")
        self._size = value
    
    def cloth_amount_calculation(self, a=1, b=1):
        return f"The needed amount of cloth for {self.name}: {self.size*a+b:.1f}"

class Suit(Clothes):
    def __init__(self, name, size):
        Clothes.__init__(self, name, size)

class Coat(Clothes):
    def __init__(self, name, size):
        Clothes.__init__(self, name, size)
        
# main
clothes = Clothes('clothes', 5)
print(clothes.cloth_amount_calculation())

suit = Suit('suit', 5)
print(suit.cloth_amount_calculation(2, 0.3))

coat = Coat('coat', 5)
print(coat.cloth_amount_calculation(1/6.5, 0.5))

