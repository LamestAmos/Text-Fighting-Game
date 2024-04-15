from fighters import *
import json

HEALTH_BAR: str = '|'

player: Player = Player(1)
enemy: Enemy = Enemy(1)
enemy.opponent = player
player.opponent = enemy


def init() -> None:
    player.do()

init()

