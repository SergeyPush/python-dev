"""
Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.
"""


class Car:
    def __init__(self, vendor, model, year) -> None:
        self.vendor = vendor
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"{self.vendor} - {self.model} - {self.year}"

    def __repr__(self) -> str:
        return f"{self.vendor} - {self.model} - {self.year}"


class Salon:
    def __init__(self) -> None:
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def sell_car(self, car):
        print(f"Selling car: {car.vendor} - {car.model} - {car.year}")
        self.cars.remove(car)

    def __str__(self) -> str:
        list_of_cars = ""
        for car in self.cars:
            list_of_cars += car.model+' '
        return list_of_cars


a1 = Car("Kia", "Cerato", 2011)
a2 = Car("Suzuki", "Vitara", 2015)
a3 = Car("BMW", "M1", 2019)

salon = Salon()
salon.add_car(a1)
salon.add_car(a2)
salon.add_car(a3)

print(salon)
salon.sell_car(a1)
print(salon)
