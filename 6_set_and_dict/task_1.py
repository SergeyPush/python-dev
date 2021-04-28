"""
Даны две строки. Выведите на экран символы, которые есть в обоих строках.
"""


def compare_strings(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    combined = set1.intersection(set2)
    return ', '.join(combined)


str1 = "abcde"
str2 = "cdefg"


print(compare_strings(str1, str2))
