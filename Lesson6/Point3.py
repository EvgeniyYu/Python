class Worker:
    def __init__(self, name, surname, position):
        self._name = name
        self._surname = surname
        self._position = position
        self.__income = {"wage": 0, "bonus": 0}

    def get_total_income(self):
        return self.__income["wage"] + self.__income["bonus"]

    def set_income(self, income, bonus):
        self.__income["wage"] = income
        self.__income["bonus"] = bonus


class Position(Worker):
    def __init__(self, name, surname, position):
        super(Position, self).__init__(name, surname, position)
    
    def get_full_name(self):
        return self._name + ' ' + self._surname


p1 = Position('John', 'McDonald', 'writer')
p1.set_income(20000, 5000)

p2 = Position('Alex', 'Pears', 'actor')
p2.set_income(30000, 20000)

p3 = Position('Cristiano', 'Ronaldo', 'football player')
p3.set_income(10000000, 5000000)

print(f'{p1.get_full_name()} has income {p1.get_total_income()}')
print(f'{p2.get_full_name()} has income {p2.get_total_income()}')
print(f'{p3.get_full_name()} has income {p3.get_total_income()}')