# Создайте Автомобиль, который может ехать.
# Ехать он может когда у него заполнен бак(переменная)
# Пользователь может заправить автомобиль, вызвав соответствующий метод,
# Поездка в зависимости от расстояния тратит топливо.
# 1(л)к10(км)

class Car:
    def __init__(self):
        self.fuel = 0

    def add_fuel(self, fuel_amount):
        self.fuel += fuel_amount

    def ride(self):
        if self.fuel > 0:
            print(f'I can ride {self.fuel*10} kilometers')
            self.fuel = 0
            return
        print('Not enough fuel')


c1 = Car()
c1.add_fuel(20)
c1.ride()
