import random
from game.components.enemies.enemy import Enemy


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

    # NEW
    def add_enemy(self):
        if len(self.enemies) < 1:
            self.enemies.append(Enemy(random.randint(0, 1)))

    def random_enemy_stats(self):
        pass            