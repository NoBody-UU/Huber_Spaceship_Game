import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.boss import Boss
from game.utils.constants import ENEMY_1, ENEMY_2, SPEED_X_1, SPEED_X_2, SPEED_Y_1, SPEED_Y_2, BOSS_1, BOSS_2

class EnemyManager:
    def __init__(self):
        self.extra_enemy_speed_x = 0
        self.extra_enemy_speed_y = 0
        self.max_enemies = 1
        self.enemies: list[Enemy] = []
        self.boss_enable = False

    def update(self, game):
        # TODO: ADD BOSS
        if ( game.score.get() % 3 == 0 and game.score.get() > 0) and not self.boss_enable:
            self.add_boss()

        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        random_enemy = self.random_enemy_stats()
        if len(self.enemies) < self.max_enemies:
            self.enemies.append(Enemy(
                image=random_enemy["image"],
                speed_y=random_enemy["speed_y"] + self.extra_enemy_speed_y,
                speed_x=random_enemy["speed_x"] + self.extra_enemy_speed_x,
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
    
    def add_boss(self):
        boss = Boss(random.choice([BOSS_1, BOSS_2]))
        self.boss_enable = True
        self.enemies.append(boss)
    
    def remove_all_enemies(self):
        self.reset()
        self.enemies = []

    # TODO: Add +1 enemy in game each 10 of score 
    def add_max_enemies(self, score):
        self.max_enemies += 1 if score % 10 == 0 or score == 5 else 0  

     # TODO: Add +1 speed in rect x,y in game each 15 of score 
    def add_more_speed(self, score):
        self.extra_enemy_speed_x += 1 if score % 15 == 0 else 0
        self.extra_enemy_speed_y += 1 if score % 15 == 0 else 0

    def reset(self):
        self.max_enemies = 1
        self.extra_enemy_speed_x = 0
        self.extra_enemy_speed_y = 0