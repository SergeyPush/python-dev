# - Язык
# - Список букв

# Для Алфавита можно:
# - Напечатать все буквы алфавита
# - Посчитать количество букв

class Alphabet:

    def __init__(self, alphabet, language):
        self.alphabet = alphabet
        self.language = language

    def __str__(self):
        return(self.alphabet)

    def __len__(self):
        list_of_items = self.alphabet.split(',')
        return len(list_of_items)


a1 = Alphabet('a,b,c', 'en')
print(a1)
print(len(a1))
