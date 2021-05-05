class Worker:
    
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = (income.get("wage"), income.get("bonus"))

class Position(Worker):
    
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
        
    def get_full_name(self):
        return self.name + ' ' + self.surname
    
    def get_total_income(self):
        return self._income[0] + self._income[1]

# main
income = {"wage": 10000, "bonus": 5000}
engineer = Position('Bob', 'Johnson', 'engineer', income)
print(f"Full name: {engineer.get_full_name()}, position: {engineer.position}, income: {engineer.get_total_income()}")
