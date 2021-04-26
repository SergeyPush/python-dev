"""
Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).
"""


class MyIterator:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.value) == 0:
            raise StopIteration
        return self.value.pop()


my_iter = MyIterator(['A', "B", "C"])

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
