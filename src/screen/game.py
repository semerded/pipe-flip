import pygame
from src import data
from src.color import Color

def game(world):
    world.cycle()
    
    if len(data.rect_update_list) != 0:
        if data.debugging:
            pygame.display.flip()
        else:
            pygame.display.update(data.rect_update_list)
        data.rect_update_list = []