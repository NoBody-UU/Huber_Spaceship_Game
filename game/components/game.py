import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, COLORS, HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, SOUND_MENU, SOUND_PLAYING, HEART, HEART_BLACK
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.counter import Counter

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.playing = False
        self.start_game = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = PowerUpManager()
        self.running = False
        self.menu = Menu(self.screen)
        self.score = Counter()
        self.higth_score = Counter()
        self.player_lifes = Counter(3)
        self.death_count = Counter()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.start_game =True
        self.reset()
        while self.playing:
            # TODO: Sound of playing
            SOUND_PLAYING.play(volume=1, loop=True, channel=2)
            SOUND_MENU.stop()
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(COLORS["WHITE"])
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_lifes()
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        SOUND_PLAYING.stop()
        SOUND_MENU.play(volume=0.5, loop=True, channel=0)
        self.menu.reset_screen_color(self.screen)

        if not self.start_game:
            self.menu.draw_texts("Press ENTER to start...", (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT - 10), self.screen)

        else:
            self.game_over()

        icon = pygame.transform.scale(ICON, (80, 120))
        icon_rect = icon.get_rect(center=(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT - 100))
        self.screen.blit(icon, icon_rect)

        self.menu.update(self)

    def set_font(self, font, size=30):
        self.font = pygame.font.Font(font, size)

    def draw_texts(self, message:str, center, color=COLORS["BLACK"]):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = center
        self.screen.blit(text, text_rect)

    def draw_score(self):
        self.draw_texts(f"Score: {self.score.get()}", (1000, 50), COLORS["WHITE"])

    # TODO: Draw lifes
    def draw_lifes(self):
        current_lives = self.player_lifes.get()
        x_offset = 20
        y = 50

        for i in range(3):
            heart_image = HEART if i < current_lives else HEART_BLACK
            icon_rect = heart_image.get_rect(center=(x_offset, y))
            self.screen.blit(heart_image, icon_rect)
            x_offset += icon_rect.width + 5


    def game_over(self):
        self.higth_score.set(self.score.get() if self.score.get() > self.higth_score.get() else self.higth_score.get())
        self.menu.draw_game_over_stats(self.higth_score.get(), self.score.get(), self.death_count.get(), self.screen)

    def reset(self):
        self.power_up_manager.reset()
        self.player.respawn(self.screen)
        self.enemy_manager.remove_all_enemies()
        self.score.reset()
        self.player_lifes.set(3)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000, 1)

            if time_to_show >= 0:
                self.menu.draw_texts(f"{self.player.power_up_type} is enable for {time_to_show} seconds", (540,50), self.screen, COLORS["WHITE"])
            else:
                self.player.has_power_up = False
                self.player.pow = DEFAULT_TYPE
                self.player.set_image()
