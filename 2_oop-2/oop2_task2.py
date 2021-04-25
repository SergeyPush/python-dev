"""
Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать нажатия мыши. Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите метод нажатия на кнопку.
"""


class GraphicalObject:
    def __init__(self, name):
        self.name = name


class Rectangle(GraphicalObject):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def display(self):
        print(f"Display {self.name} width:{self.width} height:{self.height}")


class Click:
    def click(self):
        print("Handle click button")


class Button(Rectangle, Click):

    def __init__(self, name, width, height):
        super().__init__(name, width, height)


rect = Rectangle("Rectangle", 20, 20)
rect.display()

button = Button('Submit', 20, 10)
button.click()
