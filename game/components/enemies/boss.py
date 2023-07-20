import pygame

from random import randint
from game.components.enemies.enemy import Enemy
from game.utils.constants import BOSS_LIFE, BOSS_SPEED_X, BOSS_WIDTH, BOSS_HEIGHT


class Boss(Enemy):
    def __init__(self,image, life = BOSS_LIFE):
        super().__init__(image, BOSS_SPEED_X, 1, 80, BOSS_WIDTH, BOSS_HEIGHT)
        self.life = life
        self.is_boss = True