# Создать класс "воин". Здоровье в 100 очков. В случайном порядке они
# бьют друг друга. Тот, кто бьет, здоровья не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал,
# и сколько у противника осталось здоровья. Как только у кого-то
# заканчивается ресурс здоровья, программа завершается сообщением о
# том, кто одержал победу.

from random import choice


class Warrior:
    health = 100
    opponent = None

    def __init__(self, name):
        self.name = name

    def set_opponent(self, warrior):
        self.opponent = warrior

    def hit(self):
        print(f"{self.name} attacks {self.opponent.name}")
        self.opponent.health -= 20
        print(f"{self.opponent.name}'s' helth is {self.opponent.health}")

    def __str__(self):
        return(f"{self.name} has {self.health} of healh")


w1 = Warrior("Bill")
w2 = Warrior("Bob")

w1.set_opponent(w2)
w2.set_opponent(w1)


warriors = [w1, w2]
while(True):
    selected_warrior = (choice(warriors))
    selected_warrior.hit()
    if selected_warrior.opponent.health == 0:
        print(f"{selected_warrior.name.upper()} WINS THE FIGHT!!!")
        print(w1)
        print(w2)
        break
