"""
Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год поступления на работу. Конструктор должен генерировать исключение, если заданы неправильные данные. Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты после заданного года.
"""


class WorkerException(Exception):
    pass


class Worker:
    def __init__(self, name, surname, year) -> None:
        if not name or not surname or not year:
            raise WorkerException(
                "Invalid data, enter correct name, surname and year")
        self.name = name
        self.surname = surname
        self.year = int(year)

    @classmethod
    def create_worker_from_string(cls):
        name = input("Enter name: ")
        surname = input("Enter Surname: ")
        year = input("Enter year: ")
        return cls(name, surname, year)

    def __repr__(self) -> str:
        return f"{self.name} - {self.surname} - {self.year}"

    def __str__(self) -> str:
        return f"{self.name} - {self.surname} - {self.year}"


w1 = Worker.create_worker_from_string()
w2 = Worker.create_worker_from_string()
w3 = Worker.create_worker_from_string()

workers = [w1, w2, w3]

year = 2019
for worker in workers:
    if worker.year >= year:
        print(worker)
