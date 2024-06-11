from fighters import *
import json

HEALTH_BAR: str = '|'

player: Player = Player(1)
enemy: Enemy = Enemy(1)
enemy.opponent = player
player.opponent = enemy

player_health_bar = HEALTH_BAR*int(player.hp)
enemy_health_bar = HEALTH_BAR*int(enemy.hp)


def init() -> None:
    # player.do()
    print(player_health_bar)
    print(enemy_health_bar)

init()

