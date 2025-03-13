import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pause Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

player1_keybinds = {"up": pygame.K_w, "down": pygame.K_s, "left": pygame.K_a, "right": pygame.K_d}
player2_keybinds = {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT}

# Pause menu options
options = ["Change Keybinds", "Restart Level", "Main Menu", "Volume Control", "Exit Game"]
selected_option = 0

def draw_pause_menu():
    screen.fill(BLACK)
    for i, option in enumerate(options):
        color = GREEN if i == selected_option else WHITE
        text = font.render(option, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 40))
        screen.blit(text, text_rect)

def keybind_submenu(player_keybinds, player_number):
    """
    Handles the keybind submenu for a specific player.
    
    Args:
        player_keybinds (dict): The current keybinds for the player.
        player_number (int): The player number (1 or 2).
    
    Returns:
        dict: The updated keybinds for the player.
    """
    global current_action

    # Initialize the submenu
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

        screen.fill(BLACK)
        title = font.render(f"Player {player_number} Keybinds", True, GREEN)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))

        y_offset = 150
        for action, key in player_keybinds.items():
            text = small_font.render(f"{action}: {pygame.key.name(key)}", True, WHITE)
            if action == current_action:
                pygame.draw.rect(screen, BLUE, (SCREEN_WIDTH // 2 - 150, y_offset - 5, 300, 30))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, y_offset))
            y_offset += 40

        instruction = small_font.render("Press a key to remap, ESC to go back", True, GRAY)
        screen.blit(instruction, (SCREEN_WIDTH // 2 - instruction.get_width() // 2, y_offset + 20))

        pygame.display.flip()

    return player_keybinds

def handle_input():
    global selected_option, player1_keybinds  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(options)
            elif event.key == pygame.K_RETURN:
                if options[selected_option] == "Change Keybinds":
                    player1_keybinds = keybind_submenu(player1_keybinds, 1)  
                elif options[selected_option] == "Restart Level":
                    print("Restart Level")
                elif options[selected_option] == "Main Menu":
                    print("Return to Main Menu")
                elif options[selected_option] == "Volume Control":
                    print("Adjust Volume")
                elif options[selected_option] == "Exit Game":
                    pygame.quit()
                    sys.exit()

def main():
    paused = False
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused

        if paused:
            draw_pause_menu()
            handle_input()
        else:
            screen.fill(BLACK)
            text = font.render("Game is running...", True, WHITE)
            screen.blit(text, (50, 50))

        pygame.display.flip()
        clock.tick(60)  

if __name__ == "__main__":
    main()