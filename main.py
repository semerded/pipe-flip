import pygame

# init pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("pipe flip!")

import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

# import scripts
from src import data
from src.core.utils.camera import Camera
from src.game.world import World
from src.color import Color
from src.game.input import Input
from src.core.handler.event import event_handler



data.window = pygame.display.set_mode((data.window_width, data.window_height))
data.camera = Camera(data.window_width, data.window_height)

world: World = World()
data.game_input = Input()


while data.game_running:
    data.window.fill(Color.BLACK)
    event_handler(pygame.event.get())
            
    world.draw()
    
    pygame.display.update()
            
            
# cleanup
exit(0)
