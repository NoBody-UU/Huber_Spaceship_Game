import  pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, SHIP_HEIGHT, SHIP_WIDTH

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) - SHIP_WIDTH
        self.rect.y = 500
    # NEW
    def update(self, user_input):
        movements = {
            pygame.K_LEFT: self.move_left,
            pygame.K_RIGHT: self.move_right,
            pygame.K_UP: self.move_up,
            pygame.K_DOWN: self.move_down
        }
        for key, movement in movements.items():
            if user_input[key]:
                movement()

  
    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH - SHIP_WIDTH

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.x > SCREEN_WIDTH - SHIP_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SHIP_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)