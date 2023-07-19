import random
from game.components.enemies.enemy import Enemy

from game.utils.constants import ENEMY_1, ENEMY_2, SPEED_X_1, SPEED_X_2, SPEED_Y_1, SPEED_Y_2


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        random_enemy = self.random_enemy_stats()
        if len(self.enemies) < 2:
            self.enemies.append(Enemy(
                image=random_enemy["image"],
                speed_y=random_enemy["speed_y"],
                speed_x=random_enemy["speed_x"],
                move_x_for=random_enemy["move_x_for"]
            ))

    def random_enemy_stats(self):
        enemies = [
            {
                "image": ENEMY_1,
                "speed_x": SPEED_X_1,
                "speed_y": SPEED_Y_1,
                "move_x_for": random.randint(30, 40)
            },
            {
                "image": ENEMY_2,
                "speed_x": SPEED_X_2,
                "speed_y": SPEED_Y_2,
                "move_x_for": random.randint(40, 50)
            }
        ]      
        return random.choice(enemies)
    
    def remove_all_enemies(self):
        self.enemies = []
     