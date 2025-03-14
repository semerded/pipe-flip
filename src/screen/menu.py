from src import data
from src.widgets.button import Button
from src.widgets.text import Text
from src.core.utils.screenunit import vw, vh
from src.color import Color
import pygame
from src.enums import screen, colorBlindType

font = pygame.font.SysFont("Arial", int(vw(4)))

resume_button = Button(vw(35), vh(45), vw(30), vh(11), Color.SPRING_GREEN)
resume_button.set_text("Resume", font, Color.WHITE)
main_menu_button = Button(vw(10), vh(45), vw(20), vh(11), Color.REDWOOD)
main_menu_button.set_text("Main Menu", font, Color.WHITE)
quit_button = Button(vw(70), vh(45), vw(20), vh(11), Color.REDWOOD)
quit_button.set_text("Quit :(", font, Color.WHITE)

player_1_colorblind_text = Text("colorblind mode: ", font, Color.WHITE)
player_2_colorblind_text = Text("colorblind mode: ", font, Color.WHITE)

color_blind_values = [member for member in colorBlindType]
player_1_color_blind_index = 0
player_2_color_blind_index = 0

player_1_colorblind_button = Button(vw(11) + player_1_colorblind_text.width, vh(20), vw(20), vh(10), Color.SKY_BLUE)
player_1_colorblind_button.set_text(color_blind_values[player_1_color_blind_index].value, font, Color.WHITE)
player_2_colorblind_button = Button(vw(11) + player_2_colorblind_text.width, vh(70), vw(20), vh(10), Color.SKY_BLUE)
player_2_colorblind_button.set_text(color_blind_values[player_2_color_blind_index].value, font, Color.WHITE)

def menu(player1, player2, world):
    global player_1_color_blind_index, player_2_color_blind_index
    data.window.fill(Color.BLACK)
    
    resume_button.draw()
    main_menu_button.draw()
    quit_button.draw()
    
    player_1_colorblind_text.draw(vw(10), vh(20))
    player_2_colorblind_text.draw(vw(10), vh(70))
    
    player_1_colorblind_button.draw()
    player_2_colorblind_button.draw()
    
    if resume_button.is_clicked():
        data.current_screen = screen.game
        world.update()
        
    elif main_menu_button.is_clicked():
        data.current_screen = screen.home
        
    elif quit_button.is_clicked():
        data.game_running = False
    
    elif player_1_colorblind_button.is_clicked():
        player_1_color_blind_index += 1
        
        if player_1_color_blind_index >= len(color_blind_values):
            player_1_color_blind_index = 0
        
        player1.color_blind_type = color_blind_values[player_1_color_blind_index]
        player_1_colorblind_button.set_text(color_blind_values[player_1_color_blind_index].value, font, Color.WHITE)
        
        
    elif player_2_colorblind_button.is_clicked():
        player_2_color_blind_index += 1
        
        if player_2_color_blind_index >= len(color_blind_values):
            player_2_color_blind_index = 0
        
        player2.color_blind_type = color_blind_values[player_2_color_blind_index]
        player_2_colorblind_button.set_text(color_blind_values[player_2_color_blind_index].value, font, Color.WHITE)
    
    pygame.display.flip()

