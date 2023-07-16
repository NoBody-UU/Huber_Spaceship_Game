import pygame
from pygame.sprite import Sprite
from random import randint

from game.utils.constants import ENEMY_1, ENEMY_2, SHIP_HEIGHT, SHIP_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(Sprite):
    Y_POS = 10
    SPEED_X = 5
    SPEED_Y = 1
    ENEMIES_IMG = [ENEMY_1, ENEMY_2]
    MOVEMENT_RIGHT = "right"
    MOVEMENT_LEFT = "left"
    MOV_X = {0: MOVEMENT_LEFT, 1: MOVEMENT_RIGHT}
    def __init__(self, enemy_type=0):
        self.image = self.ENEMIES_IMG[enemy_type]
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, SCREEN_WIDTH)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOV_X[randint(0, 1)]
        self.move_x_for = randint(30, 40)
        self.step = 0

    def update(self, enemies: list["Enemy"]):
        self.rect.y += self.speed_y
        if self.movement_x == self.MOVEMENT_LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        self.change_movement()

        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def change_movement(self):
        self.step = (self.step + 1) % (self.move_x_for + 1)
        if (self.step >= self.move_x_for and self.movement_x == self.MOVEMENT_RIGHT) or (self.rect.x >= SCREEN_WIDTH - SHIP_WIDTH):
            self.movement_x = self.MOVEMENT_LEFT
            self.step = 0

        elif (self.step >= self.move_x_for and self.movement_x == self.MOVEMENT_LEFT) or (self.rect.x <= 0):
            self.movement_x = self.MOVEMENT_RIGHT
            self.step = 0