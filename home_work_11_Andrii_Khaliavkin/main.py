# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб".
# Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Transport:
    def __init__(self, name, type, max_speed, max_weight, max_passengers):
        self.name = name
        self.type = type
        self.max_speed = max_speed
        self.max_weight = max_weight
        self.max_passengers = max_passengers


class Car(Transport):
    def __init__(self, name, type, max_speed, max_weight, max_passengers, max_people, max_baggage):
        super().__init__(name, type, max_speed, max_weight, max_passengers)
        self.max_people = max_people
        self.max_baggage = max_baggage


class Airplane(Transport):
    def __init__(self, name, type, max_speed, max_weight, max_passengers, max_people, max_baggage):
        super().__init__(name, type, max_speed, max_weight, max_passengers)
        self.max_people = max_people
        self.max_baggage = max_baggage

class Ship(Transport):
    def __init__(self, name, type, max_speed, max_weight, max_passengers, max_people, max_baggage):
        super().__init__(name, type, max_speed, max_weight, max_passengers)
        self.max_people = max_people
        self.max_baggage = max_baggage

car = Car('BMW', 'car', 300, 2000, 5, 5, 100)
airplane = Airplane('Boeing', 'airplane', 1000, 10000, 100, 100, 1000)
ship = Ship('Titanic', 'ship', 100, 10000, 1000, 1000, 10000)

