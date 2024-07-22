import random

class Fighter:
    def __init__(self, lvl,opponent) -> None:
        self.lvl = lvl
        self.hp = random.randint(25,30) * (.1  * lvl)
        self.speed = 10 * (.1 * lvl)
        self.defense = 15 * (.1 * lvl)
        self.attack = 20 * (.1 * lvl)
        self.opponent = opponent
        self.order = 1

    def block(self) -> None:
        print("Block")

    def dodge(self) -> None:
        print("Dodge")
    
class Player(Fighter):
    def __init__(self,lvl,opponent=None) -> None:
        super().__init__(lvl,opponent)

    def do(self) -> str:
        return input('What do you want to do: ')

    def find(self) -> None:
        print("Time to find a worthy battle")
        self.opponent.fight()

    def train(self) -> None:
        print("Train")
    
    def rest(self) -> None:
        print("Time to rest for a while....")
class Enemy(Fighter):
    def __init__(self, lvl,opponent=None) -> None:
        super().__init__(lvl,opponent)

    def fight(self) -> None:
        print("Fight")

if __name__ == "__main__":
    print("This is the fighters file")