class Car:

    # num_wheels = 4

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.num_wheels = 4

    @classmethod
    def from_string(cls, string):
        name, type = string.split(',')
        return cls(name, type)

    def __str__(self):
        return f"{self.name} - {self.type} - {self.num_wheels}"


c1 = Car("Kia", "sedan")
c2 = Car.from_string("BMW, coupe")


print(c1)
print(c2)
