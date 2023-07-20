import pygame
from game.utils.constants import FONT_STYLE, COLORS, HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT


class Menu:
    def __init__(self, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.messages = []

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.fill((255, 255, 255))
        for message in self.messages:
            self.draw_texts(message["text"], message["center"], screen, message.get("color", COLORS["BLACK"]))

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:  # Verifica que el evento sea de tipo KEYDOWN (tecla presionada)
                if event.key == pygame.K_RETURN:  # Compara el código de tecla con K_SPACE para detectar la tecla "Espacio"
                    game.run()


    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def draw_game_over_stats(self, higth_score, score, death_count, screen):
        self.reset_screen_color(screen)
        self.messages = []
        self.messages.append({"text": "GameOver. Press ENTER to restart", "center": (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT)})
        self.messages.append({"text": f"High Score: {higth_score}", "center": (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT + 35)})
        self.messages.append({"text": f"Score: {score}", "center": (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT + 65)})
        self.messages.append({"text": f"Deaths: {death_count}", "center": (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT + 95)})
        self.draw(screen)


    def draw_texts(self, message, center, screen, color=COLORS["BLACK"]):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect(center=center)
        screen.blit(text, text_rect)
