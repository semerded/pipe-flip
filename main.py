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
from src.game.player import Player
from src.core.handler.scaling import Scaling

data.window = pygame.display.set_mode((data.window_width, data.window_height), pygame.HWSURFACE | pygame.DOUBLEBUF)
data.camera = Camera(data.window_width, data.window_height)

data.game_input = Input()

data.clock = pygame.time.Clock()

player1 = Player(data.game_input, "assets/img/actor/player.png", False, 0)
player2 = Player(data.game_input, "assets/img/actor/player.png", True, 1)

world: World = World(player1, player2)
world.update()

while data.game_running:
    print(data.clock.get_fps())
    data.clock.tick(data.FPS)
    # data.window.fill(Color.BLACK)
    event_handler(pygame.event.get())
            
    world.cycle()
    
    if len(data.rect_update_list) != 0:
        pygame.display.update(data.rect_update_list)
        data.rect_update_list = []
            
            
# cleanup
exit(0)
