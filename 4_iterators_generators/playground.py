class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __getitem__(self):
        return self.value

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


my_range = MyRange(1, 10)

print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))


def my_range(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


my_nums = my_range(1, 5)
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

print(dir(my_nums))
