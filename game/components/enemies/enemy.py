import pygame
from pygame.sprite import Sprite
from random import randint

from game.utils.constants import ENEMY_1, SHIP_HEIGHT, SHIP_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, BOOM, SOUND_KILL
from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    Y_POS = 10
    MOVEMENT_RIGHT = "right"
    MOVEMENT_LEFT = "left"
    MOV_X = {0: MOVEMENT_LEFT, 1: MOVEMENT_RIGHT}
    def __init__(self, image=ENEMY_1, speed_x= 5, speed_y=1, move_x_for=randint(30, 40), with_enemy=SHIP_WIDTH, height_enemy=SHIP_HEIGHT):
        self.width = with_enemy
        self.height = height_enemy
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, SCREEN_WIDTH)
        self.rect.y = self.Y_POS

        self.speed_x = speed_x
        self.speed_y = speed_y
        self.movement_x = self.MOV_X[randint(0, 1)]
        self.move_x_for = move_x_for
        self.step = 0
        self.type = "enemy"
        self.shooting_time = pygame.time.get_ticks() + randint(200, 500)
        self.life = 1
        self.is_boss = False

    def update(self, enemies: list["Enemy"], game):
        self.rect.y += self.speed_y if not self.is_boss else 0
        self.shoot(game.bullet_manager)

        if self.movement_x == self.MOVEMENT_LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        self.change_movement()
        
        
        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)
    
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if current_time >= self.shooting_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time = current_time + randint(1000, 2000)



    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def change_movement(self):
        self.step += 1
        if (self.step >= self.move_x_for and self.movement_x == self.MOVEMENT_RIGHT) or (self.rect.x >= SCREEN_WIDTH - self.width):
            self.movement_x = self.MOVEMENT_LEFT
            self.step = 0

        elif (self.step >= self.move_x_for and self.movement_x == self.MOVEMENT_LEFT) or (self.rect.x <= 0):
            self.movement_x = self.MOVEMENT_RIGHT
            self.step = 0

    # TODO: SHOW IMAGE WHEN ENEMY IS DESTROYED
    def destroy(self, game):
        SOUND_KILL.play(loop=False, channel=1)
        explosion_image = pygame.transform.scale(BOOM, (self.width, self.height))
        game.screen.blit(explosion_image, self.rect)
        pygame.display.flip()
        game.enemy_manager.enemies.remove(self)
        game.score.add()