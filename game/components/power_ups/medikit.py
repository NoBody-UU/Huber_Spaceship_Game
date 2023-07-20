import pygame

from game.components.power_ups.power_up import PowerUp
from game.utils.constants import MEDIKIT_TYPE, MEDIKIT


class MediKit(PowerUp):
    def __init__(self):
        super().__init__(MEDIKIT, MEDIKIT_TYPE)