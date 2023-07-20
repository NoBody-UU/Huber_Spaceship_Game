import pygame

class BulletManager:
    
    def __init__(self):
        self.bullets = []
        self.enemy_bullets  = []
 
    def update(self, game):
        # * Enemies Bullets
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == "enemy":
                self.enemy_bullets.remove(bullet)
                game.playing = game.player_lifes.get() >= 2
                if not game.player.has_power_up:                   
                     game.player_lifes.rest()
                     game.death_count.add()
                     pygame.time.delay(1000)
                     break

         # * Player Bullets   
        for bullet in self.bullets: 
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == "player":
                    if bullet in self.bullets: 
                        self.bullets.remove(bullet)
                    enemy.life -= 1
                    if enemy.life <= 0:
                        game.enemy_manager.boss_enable = False if enemy.is_boss and game.enemy_manager.boss_enable else game.enemy_manager.boss_enable
                        enemy.destroy(game)
                        # TODO: Add game difficulty
                        game.enemy_manager.add_more_speed(game.score.get())
                        game.enemy_manager.add_max_enemies(game.score.get())

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    
    def add_bullet(self, bullet):
        if bullet.owner == "enemy":
            self.enemy_bullets.append(bullet)
        elif bullet.owner == "player" and len(self.bullets) < 3:
            self.bullets.append(bullet)
