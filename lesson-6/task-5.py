class Stationery:
    
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print("Start of draw")

class Pen(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print(f"The draw of {self.title} starts")

class Pencil(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print(f"The draw of {self.title} starts")
        
class Handle(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print(f"The draw of {self.title} starts")
    
# main
pen = Pen("Bic")
pen.draw()
pencil = Pencil("Apple")
pencil.draw()
handle = Handle("Brauberg")
handle.draw()
