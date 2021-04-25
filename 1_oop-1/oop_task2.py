"""
Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов.
Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.
"""


class Book:

    def __init__(self, author, name, year) -> None:
        self.author = author
        self.name = name
        self.year = year
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def __str__(self) -> str:
        list_of_reviews = ", ".join(self.reviews)
        return f"{self.author} {self.name} {self.year}. Reviews: {list_of_reviews}"

    def __str__(self) -> str:
        return f"{self.author} - {self.title} - {self.year} - {self.genre}"


b1 = Book("Kafka", "Castle", 1985)
b1.add_review("Normal book")
b1.add_review("Don't like it")

print(b1)
