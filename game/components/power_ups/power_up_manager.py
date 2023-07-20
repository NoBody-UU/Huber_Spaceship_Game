import pygame

from random import randint, choice
from game.components.power_ups.shield import Shield
from game.components.power_ups.medikit import MediKit
from game.utils.constants import SPACESHIP_SHIELD, MEDIKIT_TYPE, SOUND_POWER_UP


class PowerUpManager:
    
    def __init__(self):
        self.power_ups: list[Shield]= []
        self.when_appears = randint(5000, 10000)
        self.duration = randint(3, 5)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                # TODO: POWER UPS
                if power_up.type == MEDIKIT_TYPE:
                    if game.player_lifes.get() < 3:
                        game.player_lifes.add()
                else:
                  power_up.start_time = pygame.time.get_ticks()
                  game.player.power_up_type = power_up.type
                  game.player.has_power_up = True
                  game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                  game.player.set_image((65, 75), SPACESHIP_SHIELD)

                SOUND_POWER_UP.play(loop=False, channel=1)

                self.power_ups.remove(power_up)

    def generate_power_up(self):
        power_ups = [
            Shield(),
            MediKit()
        ]
        power_up = choice(power_ups)
        self.when_appears += randint(5000, 10000)
        self.power_ups.append(power_up)
        

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = randint(now + 5000, max(now + 5000, self.when_appears + 5000))