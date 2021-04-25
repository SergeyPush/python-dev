"""
Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе издания и жанре. 
Создайте несколько разных книг. 
Определите для него операции проверки на равенство и неравенство, методы __repr__ и __str__.
"""


class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __repr__(self) -> str:
        return f"{self.author} - {self.title} - {self.year} - {self.genre}"

    def __str__(self) -> str:
        return f"{self.author} - {self.title} - {self.year} - {self.genre}"

    def __eq__(self, o: object) -> bool:
        return self.title == o.title and self.author == o.author

    def __ne__(self, o: object) -> bool:
        return self.title != o.title


b1 = Book("Castle", "Kafka", 1943, 'Novel')
b2 = Book("Pharaon", "Prus", 1986, "Novel")

print(b1)
print(b2)

b3 = b1

print(b1 == b2)
print(b1 == b3)
print(b1 != b2)
