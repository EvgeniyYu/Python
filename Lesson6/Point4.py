import random, time

class Car:
    def __init__(self, color, name, is_police = False):
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        _speed = random.random() * 100
        print(f'Car {self.name}: {_speed}')

    def go(self):
        return True

    def stop(self):
        return False

    def turn(self):
        #1 - FORWARD, 2 - LEFT, 3 - RIGHT, 4 - BACK
        return 1

class TownCar(Car):
    def __init__(self, color, name, is_police = False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        _speed = random.random() * 100
        if _speed > 60:
            print(f'TownCar: {self.name}: speed over {_speed}')
        else:
            print(f'TownCar: {self.name}: {_speed}')



class SportCar(Car):
    def __init__(self, color, name, is_police = False):
        super().__init__(color, name, is_police)
    #def show_speed(self):
    #    super().show_speed()

class WorkCar(Car):
    def __init__(self, color, name, is_police = False):
        super().__init__(color, name, is_police )

    def show_speed(self):
        _speed = random.random() * 100
        if _speed > 40:
            print(f'WorkCar: {self.name}: speed over {_speed}')
        else:
            print(f'WorkCar: {self.name}: {_speed}')

class PoliceCar(Car):
    def __init__(self, color, name, is_police = False):
        super().__init__(color, name, is_police )


car1 = TownCar('black', 'BMW', False)
car2 = PoliceCar('blue', 'Opel', True)
car3 = SportCar('red', 'Ferrari', False)
car4 = WorkCar('white', 'volkswagen', False)
car5 = TownCar('black', 'Audi', False)

while True:
    car1.show_speed()
    car2.show_speed()
    car3.show_speed()
    car4.show_speed()
    car5.show_speed()
    time.sleep(3)