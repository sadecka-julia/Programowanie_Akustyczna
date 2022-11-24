from enum import Enum


class Type(Enum):
    CAR = 1
    TRUCK = 2
    MOTOR = 3


class Car(Type):
    def __init__(self, regist_num, color, type):
        self.regist_num = regist_num
        self.color = color
        if type == 'car':
            self.type = Type.CAR
        elif type == 'truck':
            self.type = Type.TRUCK
        elif type == 'motor':
            self.type = Type.MOTOR

    def car_info(self):
        return f'Car information: 1. Registration number: {self.regist_num} 2. Color: {self.color} 3. Type: {self.type}'

    def entrance(self):
        return 1

    def exit(self):
        return -1


class Parking(Car):
    def __init__(self, regist_num, color, type):
        Car.__init__(self, regist_num, color, type)
        self.taken_spaces = 0
        self.take = 0
        self.__num_of_spaces = 5
        # tworzę słownik, który przechowuje informację o zaparkowanych samochodach
        self.car_record = {'registration number': [], 'color': [], 'type': []}
