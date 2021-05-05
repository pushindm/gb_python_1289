class Car:
    
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police 
    
    def go(self):
        msg = f"The car {self._name} is moving" if self.speed != 0 else f"The car {self._name} has stopped"
        print(msg)
    
    def turn(self, direction):
        if self.speed != 0:
            print(f"The car {self._name} is moving in {direction} direction with {self.speed} km/h") 
        else: 
            print(f"The car {self._name} is not moving")
    
    def show_speed(self):
        print(f"The current speed of car {self._name}: {self.speed}")
    
    def check_type(self):
        msg = f"The {self._name} is a police car" if self._is_police else f"The {self._name} is not a police car" 
        print(msg)

class TownCar(Car):
    
    __speed_limit = 60
    
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    
    def show_speed(self):
        if self.speed > TownCar.__speed_limit:
            print(f"The current speed {self.speed} km/h of {self._name} is more that limit: {TownCar.__speed_limit} km/h")
        else:
            print(f"The current speed of {self._name}: {self.speed}")
            
class WorkCar(Car):
    
    __speed_limit = 40
    
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    
    def show_speed(self):
        if self.speed > WorkCar.__speed_limit:
            print(f"The current speed {self.speed} km/h of {self._name} is more that limit: {WorkCar.__speed_limit} km/h")
        else:
            print(f"The current speed of {self._name}: {self.speed}")

class SportCar(Car):
    
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class PoliceCar(Car):
    
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

# main
town_car = TownCar(70, "black", "Toyota")
town_car.turn("left")
town_car.show_speed()
town_car.speed = 40
town_car.show_speed()

work_car = WorkCar(30, "red", "Volvo")
work_car.turn("right")
work_car.show_speed()

sport_car = SportCar(0, "white", "Porshe")
print(f"Info: {sport_car._name} {sport_car._color}")
sport_car.go()

police_car = PoliceCar(40, "white", "Ford")
police_car.check_type()
