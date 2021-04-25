"""
Создайте функцию от произвольного количества аргументов, которая вычисляет среднее арифметическое данных чисел. 
Вычислите при помощи неё среднее арифметическое двух заданных чисел и среднее арифметическое чисел из заданного диапазона.
"""


def middle_arithmetic(*args):
    return sum(args)/len(args)


res1 = middle_arithmetic(1, 2, 3, 4, 5, 6)
res2 = middle_arithmetic(*range(1, 7))

print(res1)
print(res2)
