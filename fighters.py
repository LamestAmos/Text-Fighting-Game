import random

class Fighter:
    def __init__(self, lvl,opponent):
        self.lvl = lvl
        self.hp = 30 * (.1 * lvl)
        self.speed = 10 * (.1 * lvl)
        self.defense = 15 * (.1 * lvl)
        self.attack = 20 * (.1 * lvl)
        self.opponent = opponent
        self.order = 1

    def block(self):
        print("Block")

    def dodge(self):
        print("Dodge")


class Player(Fighter):
    def __init__(self,lvl,opponent=None):
        super().__init__(lvl,opponent)

    def do(self):
        return input('What do you want to do: ')

    def find(self):
        print("Time to find a worthy battle")
        self.opponent.fight()

    def train(self):
        print("Train")

class Enemy(Fighter):
    def __init__(self, lvl,opponent=None):
        super().__init__(lvl,opponent)

    def fight(self):
        print("Fight")

