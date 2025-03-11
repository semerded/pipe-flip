import pygame
from src import data
from src.game.input import Input

def event_handler(event):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            data.game_running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                data.game_running = False
            
            if event.key == pygame.K_j:
                data.game_input.player_left(0)
            if event.key == pygame.K_l:
                data.game_input.player_right(0)
            if event.key == pygame.K_i:
                data.game_input.player_jump(0)
            
            if event.key == pygame.K_q:
                data.game_input.player_left(1)
            if event.key == pygame.K_d:
                data.game_input.player_right(1)
            if event.key == pygame.K_z:
                data.game_input.player_jump(1)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_j:
                data.game_input.player_cancel_left(0)
            if event.key == pygame.K_l:
                data.game_input.player_cancel_right(0)
            if event.key == pygame.K_i:
                data.game_input.player_cancel_jump(0)
            
            if event.key == pygame.K_q:
                data.game_input.player_cancel_left(1)
            if event.key == pygame.K_d:
                data.game_input.player_cancel_right(1)
            if event.key == pygame.K_z:
                data.game_input.player_cancel_jump(1)