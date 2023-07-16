import random
from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []
        self.count = 0

    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    # NEW
    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy_type = 1 if self.count == 2 else 0
            self.enemies.append(Enemy(enemy_type))
            self.count = (self.count + 1) % 3