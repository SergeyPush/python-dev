"""
Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть реализована возможность ввода изначальной ссылки и короткого названия и получения изначальной ссылки по её названию.
"""


class Shortener:

    def __init__(self):
        self.links = {}

    def add_link(self, link, key):
        self.links.update({key: link})

    def get_item(self, key):
        if key not in self.links:
            print("Invalid key")
            return

        print(f"{key}: {self.links.get(key)}")

    def get_all_items(self):
        for k, v in self.links.items():
            print(f"{k}: {v}")


shortener = Shortener()
shortener.add_link("http://google.com", 'ggl')
shortener.add_link("http://amazon.com", 'amz')
shortener.add_link("http://ebay.com", 'eby')

shortener.get_all_items()
shortener.get_item("aby")
shortener.get_item("eby")
