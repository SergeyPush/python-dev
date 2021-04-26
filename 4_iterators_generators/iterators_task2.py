"""
Перепишите решение первого задания с помощью генератора.
"""


def my_generator(values):
    list_of_items = values
    while len(list_of_items) > 0:
        yield list_of_items.pop()


my_gen = my_generator(['A', "B", "C"])


print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
