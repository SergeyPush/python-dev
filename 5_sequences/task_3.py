"""
Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова данного текста.
"""


def sorted_text(user_input):
    text = user_input.split(" ")
    return sorted(text)


text = input("Enter some text: ")
print(sorted_text(text))
