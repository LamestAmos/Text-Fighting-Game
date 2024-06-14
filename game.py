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
    while True:
        player_decision: str = player.do().lower()
        # print(player_health_bar)
        # print(enemy_health_bar)

        if player_decision == "rest":
            print("Time to rest for a while....")
            break

init()

