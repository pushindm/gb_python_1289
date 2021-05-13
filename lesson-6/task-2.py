class Road:
    
    _length = 1 # m
    _width = 1 # m
    
    def __init__(self, length, width, height=5, mass=25):
        Road._length = length
        Road._width = width
        self.height = height
        self.mass = mass
    
    def calc_costs(self):
        return f"The required mass of asphalt for road creation: {Road._length*Road._width*self.height*0.001*self.mass:.0f} tons"

# main
road = Road(5000,20)
print(road.calc_costs())
