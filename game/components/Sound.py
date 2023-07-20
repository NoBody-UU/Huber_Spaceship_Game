import pygame

# TODO:  CLASS TO MANAGE SOUNDS
class SoundManager:
    def __init__(self, sound_file):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(sound_file)
        self.channel = None
        self.is_looping = False

    def play(self, volume=1.0, loop=False, channel=None):
        self.set_volume(volume)
        if loop:
            if not self.is_looping:
                self.channel = pygame.mixer.Channel(channel) if channel is not None else pygame.mixer.find_channel()
                # Usamos loops=-1 para que el sonido se reproduzca en bucle continuo
                self.channel.play(self.sound, loops=-1, fade_ms=2000)
                self.is_looping = True
        else:
            self.channel = pygame.mixer.Channel(channel) if channel is not None else pygame.mixer.find_channel()
            self.channel.play(self.sound)

    def stop(self):
        if self.channel is not None:
            self.channel.stop()
            self.is_looping = False

    def set_volume(self, volume):
        self.sound.set_volume(volume)

    def get_is_looping(self):
        return self.is_looping
