from fighters import *
import json

HEALTH_BAR: str = '|'

player: Player = Player(1)
enemy: Enemy = Enemy(1)
enemy.opponent = player
player.opponent = enemy

player_health_bar: str = HEALTH_BAR*int(player.hp)
enemy_health_bar: str = HEALTH_BAR*int(enemy.hp)

def init() -> None:
    print("""
    Welcome to the text fighting game where you train and fight enemies to be stronger
          Commands for the game are:
            find
            train
            rest
    """)
    while True:
        player_decision: str = player.do().lower()
        # print(player_health_bar)
        # print(enemy_health_bar)
        if player_decision == "find":
            player.find()

        elif player_decision == "train":
            player.train()

        elif player_decision == "rest":
            player.rest()
            break

        else:
            print("Invalid command!")

init()

