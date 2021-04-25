"""
Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание, умножение, деление и возведение в степень. 
Программа должна выдавать сообщения об ошибке и продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в отрицательную степень.
"""


class Calc:
    def sum(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mult(self, a, b):
        return a*b

    def div(self, a, b):
        try:
            res = a/b
        except ZeroDivisionError:
            return "Cannot divide by Zero"
        return res

    def pow(self, number, power):
        try:
            return number**power
        except ZeroDivisionError:
            return "Impossible to perform operation with these arguments"


calc = Calc()
sum = calc.sum(1, 2)
print(sum)
sub = calc.div(2, 1)
print(sub)
mult = calc.mult(2, 2)
print(mult)
div = calc.div(2, 0)
print(div)
pow = calc.pow(0, -1)
print(pow)
