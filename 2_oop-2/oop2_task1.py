"""
Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод edit_document выводит на экран информацию о том, что редактирование документов недоступно для бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён. Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor, иначе Editor. Вызовите методы просмотра и редактирования документов.
"""


class Editor:

    def view_document(self):
        print("View document")

    def edit_document(self):
        print("Edit document is available only for Pro version")


class ProEditor(Editor):
    def edit_document(self):
        print("Edit document")


license_key = "12345"


user_key = input("Enter license key: ")


if (license_key == user_key):
    editor = ProEditor()
else:
    editor = Editor()
editor.view_document()
editor.edit_document()
