# Создать рабочего. У который может ходить на работу.
# Рабочий должен иметь возраст и имя.
# Так же принимать решение идти на работу или нет, в зависимости от того,
# какой ему передали номер дня

class Worker:

    working_days = [1, 2, 3, 4, 5]

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def go_to_work(self, day):
        if day in self.working_days:
            print(f"{self.name} is working today")
        else:
            print(f"Today is dayoff")


w1 = Worker('George', 32)
w1.go_to_work(3)
w1.go_to_work(6)
