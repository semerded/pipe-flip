import pygame

# init pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("pipe flip!")

# import scripts
from src import data
from src.core.utils.camera import Camera
from src.game.world import draw_world
from src.color import Color



data.window = pygame.display.set_mode((data.window_width, data.window_height))
data.camera = Camera(data.window_width, data.window_height)


while data.game_running:
    data.window.fill(Color.BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            data.game_running = False
            
    draw_world()
    
    pygame.display.update()
            
            
# cleanup
exit(0)
