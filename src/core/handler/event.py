import pygame
from src import data
from src.game.input import Input
from src.enums import screen

def event_handler(event):
    data.game_input.reset_mouse_button_flank()
    for _event in event:
        if _event.type == pygame.QUIT:
            data.game_running = False
            
        elif _event.type == pygame.KEYDOWN:
            if _event.key == pygame.K_ESCAPE:
                data.current_screen = screen.menu
            
            if _event.key == pygame.K_j:
                data.game_input.player_left(0)
            if _event.key == pygame.K_l:
                data.game_input.player_right(0)
            if _event.key == pygame.K_i:
                data.game_input.player_jump(0)
            
            if _event.key == pygame.K_q:
                data.game_input.player_left(1)
            if _event.key == pygame.K_d:
                data.game_input.player_right(1)
            if _event.key == pygame.K_z:
                data.game_input.player_jump(1)
            
        elif _event.type == pygame.KEYUP:
            if _event.key == pygame.K_j:
                data.game_input.player_cancel_left(0)
            if _event.key == pygame.K_l:
                data.game_input.player_cancel_right(0)
            if _event.key == pygame.K_i:
                data.game_input.player_cancel_jump(0)
            
            if _event.key == pygame.K_q:
                data.game_input.player_cancel_left(1)
            if _event.key == pygame.K_d:
                data.game_input.player_cancel_right(1)
            if _event.key == pygame.K_z:
                data.game_input.player_cancel_jump(1)
                
        if _event.type == pygame.MOUSEBUTTONDOWN:
            if _event.button == 1:
                data.game_input.lmb_status = True
                data.game_input.lmb_flank = True
                
        elif _event.type == pygame.MOUSEBUTTONUP:
            if _event.button == 1:
                data.game_input.lmb_status = False
                data.game_input.lmb_flank = True
                
                