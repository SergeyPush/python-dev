"""
Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства. 
Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в одной шкале, а получены в другой.
"""


class Temperature:
    def __init__(self, celsius=0, farenheit=0):
        self._celsius = celsius
        self._farenheit = farenheit

    @property
    def celsius(self):
        return self.farenheit_to_celsius(self._farenheit)

    @property
    def farenheit(self):
        return self.celcius_to_farenheit(self._celsius)

    def celcius_to_farenheit(self, celcius):
        return (celcius*9/5)+32

    def farenheit_to_celsius(self, farenheit):
        return (farenheit-32)*5/9


t1 = Temperature(celsius=20)
print(t1.farenheit)
t2 = Temperature(farenheit=32)
print(t2.celsius)
