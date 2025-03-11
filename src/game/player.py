import pygame
from src.enums import colorBlindType

class Player:
    def __init__(self, img: str, upside_down: bool):
        self.color_blind_type = colorBlindType.none
        
        self.score = 0
        self.upside_down = upside_down
        self.img = pygame.transform.flip(pygame.image.load(img), False, upside_down)
        
    def change_chunk(self):
        self.upside_down = not self.upside_down
        self.img = pygame.transform.flip(self.img, False, self.upside_down)
        
    