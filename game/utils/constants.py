import pygame
import os

from game.components.Sound import SoundManager

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SHIP_WIDTH = 40
SHIP_HEIGHT = 60

# Default Stast For Enemies
BOSS_LIFE = 7
BOSS_SPEED_X = 7
BOSS_WIDTH = 240
BOSS_HEIGHT = 250
BOSS_SIZE = (BOSS_HEIGHT, BOSS_WIDTH)
SPEED_X_1 = 5
SPEED_Y_1 = 1
SPEED_X_2 = 6
SPEED_Y_2 = 2

# Colors
COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0)
}

# Sounds
SOUND_MENU = SoundManager(os.path.join(IMG_DIR, "Sounds/menu.mp3"))
SOUND_PLAYING = SoundManager(os.path.join(IMG_DIR, "Sounds/playing.mp3"))
SOUND_POWER_UP = SoundManager(os.path.join(IMG_DIR, "Sounds/power_up.mp3"))
SOUND_KILL = SoundManager(os.path.join(IMG_DIR, "Sounds/kill.mp3"))

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART_BLACK = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeartBlack.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

MEDIKIT = pygame.image.load(os.path.join(IMG_DIR, 'Other/medikit.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
MEDIKIT_TYPE = "medikit"

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
BOSS_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/boss_1.png"))
BOSS_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/boss_2.png"))

BOOM = pygame.image.load(os.path.join(IMG_DIR, 'Other/boom.png'))

FONT_STYLE = 'freesansbold.ttf'
