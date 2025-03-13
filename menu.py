import pygame
pygame.init()

from src import data
import sys
from src.enums import colorBlindType

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pause Menu")

class GameInput:
    def is_mouse_clicked_in_rect(self, rect):
        mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(mouse_pos)

from src.widgets.button import Button 
import src.data

src.data.window = screen
src.data.game_input = GameInput()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

player1_keybinds = {"up": pygame.K_w, "down": pygame.K_s, "left": pygame.K_a, "right": pygame.K_d, "enter": pygame.K_SPACE}
player2_keybinds = {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "enter": pygame.K_RETURN}

options = ["Change Keybinds", "Main Menu", "Exit Game", "Colorblind Mode"]
selected_option = {1: 0, 2: 0}
input_cooldown = {1: 0, 2: 0}
COOLDOWN_TIME = 10
COLORBLIND_COOLDOWN_TIME = 30

current_colorblind_type = {1: colorBlindType.none, 2: colorBlindType.none}

active_submenu_player = None

pause_button = Button(
    x=SCREEN_WIDTH - 100,
    y=10,
    width=90,
    height=40,
    color=GRAY,
    border_radius=-1
)
pause_button.set_text("Pause", font, BLACK)

def draw_menu(player, y_offset):
    for i, item in enumerate(options):
        color = GREEN if i == selected_option[player] else WHITE
        text = font.render(item, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
        screen.blit(text, text_rect)
        y_offset += 40
    
    colorblind_text = f"Colorblind: {current_colorblind_type[player].name}"
    colorblind_label = small_font.render(colorblind_text, True, GREEN if current_colorblind_type[player] != colorBlindType.none else GRAY)
    colorblind_rect = colorblind_label.get_rect(center=(SCREEN_WIDTH // 2, y_offset + 20))
    screen.blit(colorblind_label, colorblind_rect)
    
    enter_button_text = f"Press {pygame.key.name(player1_keybinds['enter'] if player == 1 else player2_keybinds['enter'])} to select"
    enter_text = small_font.render(enter_button_text, True, GRAY)
    enter_rect = enter_text.get_rect(center=(SCREEN_WIDTH // 2, y_offset + 50))
    screen.blit(enter_text, enter_rect)

def keybind_submenu(player_keybinds, player_number):
    global active_submenu_player
    submenu_active = True
    current_action = "up"
    
    while submenu_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    submenu_active = False
                else:
                    player_keybinds[current_action] = event.key
                    actions = list(player_keybinds.keys())
                    current_index = actions.index(current_action)
                    if current_index < len(actions) - 1:
                        current_action = actions[current_index + 1]
                    else:
                        submenu_active = False
        
        if player_number == 1:
            screen_region = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT // 2)
        else:
            screen_region = pygame.Rect(0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2)
        
        screen.fill(BLACK, screen_region)
        title = font.render(f"Player {player_number} Keybinds", True, GREEN)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50 if player_number == 1 else SCREEN_HEIGHT // 2 + 50))
        
        y_offset = 150 if player_number == 1 else SCREEN_HEIGHT // 2 + 150
        for action, key in player_keybinds.items():
            text = font.render(f"{action}: {pygame.key.name(key)}", True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            screen.blit(text, text_rect)
            y_offset += 40
        
        pygame.display.update(screen_region)
    
    active_submenu_player[player_number] = False
    return player_keybinds

def colorblind_submenu(player):
    global current_colorblind_type, active_submenu_player
    submenu_active = True
    colorblind_options = list(colorBlindType)
    selected_colorblind_option = colorblind_options.index(current_colorblind_type[player])
    
    while submenu_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    submenu_active = False
                elif event.key == (player1_keybinds["up"] if player == 1 else player2_keybinds["up"]):
                    selected_colorblind_option = (selected_colorblind_option - 1) % len(colorblind_options)
                elif event.key == (player1_keybinds["down"] if player == 1 else player2_keybinds["down"]):
                    selected_colorblind_option = (selected_colorblind_option + 1) % len(colorblind_options)
                elif event.key == (player1_keybinds["enter"] if player == 1 else player2_keybinds["enter"]):
                    current_colorblind_type[player] = colorblind_options[selected_colorblind_option]
                    submenu_active = False
        
        if player == 1:
            screen_region = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT // 2)
        else:
            screen_region = pygame.Rect(0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2)
        
        screen.fill(BLACK, screen_region)
        title = font.render(f"Player {player} Colorblind Settings", True, GREEN)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50 if player == 1 else SCREEN_HEIGHT // 2 + 50))
        
        y_offset = 150 if player == 1 else SCREEN_HEIGHT // 2 + 150
        for i, option in enumerate(colorblind_options):
            color = GREEN if option == current_colorblind_type[player] else GRAY
            text = font.render(option.name, True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            screen.blit(text, text_rect)
            y_offset += 40
        
        enter_button_text = f"Press {pygame.key.name(player1_keybinds['enter'] if player == 1 else player2_keybinds['enter'])} to select"
        enter_text = small_font.render(enter_button_text, True, GRAY)
        enter_rect = enter_text.get_rect(center=(SCREEN_WIDTH // 2, y_offset + 20))
        screen.blit(enter_text, enter_rect)
        
        pygame.display.update(screen_region)
    
    active_submenu_player[player] = False

def execute_option(player, option):
    global player1_keybinds, player2_keybinds, active_submenu_player
    if option == "Change Keybinds":
        active_submenu_player[player] = True
        if player == 1:
            player1_keybinds = keybind_submenu(player1_keybinds, 1)
        else:
            player2_keybinds = keybind_submenu(player2_keybinds, 2)
        active_submenu_player[player] = False
    elif option == "Main Menu":
        print(f"Player {player} returning to Main Menu")
    elif option == "Exit Game":
        pygame.quit()
        sys.exit()
    elif option == "Colorblind Mode":
        active_submenu_player[player] = True
        colorblind_submenu(player)
        active_submenu_player[player] = False  

def handle_input(event, player):
    global selected_option, input_cooldown, active_submenu_player
    
    if input_cooldown[player] > 0 or active_submenu_player[player]:
        return
    
    if event.type == pygame.KEYDOWN:
        if event.key == (player1_keybinds["up"] if player == 1 else player2_keybinds["up"]):
            selected_option[player] = (selected_option[player] - 1) % len(options)
            input_cooldown[player] = COOLDOWN_TIME
        elif event.key == (player1_keybinds["down"] if player == 1 else player2_keybinds["down"]):
            selected_option[player] = (selected_option[player] + 1) % len(options)
            input_cooldown[player] = COOLDOWN_TIME
        elif event.key == (player1_keybinds["enter"] if player == 1 else player2_keybinds["enter"]):
            execute_option(player, options[selected_option[player]])

active_submenu_player = {1: False, 2: False}

def handle_input(event, player):
    global selected_option, input_cooldown, active_submenu_player
    
    if input_cooldown[player] > 0 or active_submenu_player[player]:
        return
    
    if event.type == pygame.KEYDOWN:
        if event.key == (player1_keybinds["up"] if player == 1 else player2_keybinds["up"]):
            selected_option[player] = (selected_option[player] - 1) % len(options)
            input_cooldown[player] = COOLDOWN_TIME
        elif event.key == (player1_keybinds["down"] if player == 1 else player2_keybinds["down"]):
            selected_option[player] = (selected_option[player] + 1) % len(options)
            input_cooldown[player] = COOLDOWN_TIME
        elif event.key == (player1_keybinds["enter"] if player == 1 else player2_keybinds["enter"]):
            execute_option(player, options[selected_option[player]])

def main():
    global active_submenu_player
    paused = False
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = not paused
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and pause_button.is_clicked():
                    paused = not paused
            
            if paused:
                handle_input(event, 1)
                handle_input(event, 2)
        
        for player in input_cooldown:
            if input_cooldown[player] > 0:
                input_cooldown[player] -= 1

        if paused:
            screen.fill(BLACK)
            draw_menu(1, 50)
            draw_menu(2, SCREEN_HEIGHT - 200)
            pygame.draw.line(screen, WHITE, (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2), 2)
        else:
            screen.fill(BLACK)
            text = font.render("Game is running...", True, WHITE)
            screen.blit(text, (50, 50))
            pause_button.draw()
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
