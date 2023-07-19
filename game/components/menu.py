import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.update_message(message)
        self.messages = []

    # ! Change
    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
        for message in self.messages:
            self.draw_texts(message["text"], message["center"], screen, message.get("color", (0, 0, 0)))

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def draw_game_over_stats(self, higth_score, score, death_count, screen):
        self.reset_screen_color(screen)
        self.update_message(" GameOver. Press any key to restart")
        self.messages = []
        self.messages.append({"text": f"High Score: {higth_score}", "center": (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)})
        self.messages.append({"text": f"Score: {score}", "center": (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)})
        self.messages.append({"text": f"Deaths: {death_count}", "center": (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 90)})


    def draw_texts(self, message, center, screen, color=(0, 0, 0)):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect(center=center)
        screen.blit(text, text_rect)
