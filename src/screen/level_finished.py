import pygame
from src import data
from src.color import Color
from src.enums import screen

# Global variables for the level and score
level = 1  # Example initial level
score = 0  # Example initial score

# Font: Increased size and set to bold
font = pygame.font.Font(None, 72)  # 72px font size, adjust as needed
font_bold = pygame.font.Font(None, 72)  # Bold font, same size

# Set the font to bold
font_bold.set_bold(True)

def level_finished():
    """
    Displays the level completed screen with level details and options to proceed.
    This version doesn't require arguments, using global variables for level and score.
    """
    data.window.fill(Color.BLACK)
    # Load and display the background image first
    try:
        background_image = pygame.image.load('./assets/img/finish.jpeg')
        background_image = pygame.transform.scale(background_image, (data.window_width, data.window_height))
        background_image = background_image.convert_alpha()
        background_image.set_alpha(128)
        data.window.blit(background_image, (0, 0))
    except pygame.error as e:
        print(f"Error loading image: {e}")

    # Create the title text (bold and larger)
    title_text = "Level Completed!"
    title_surface = font_bold.render(title_text, True, Color.WHITE)
    title_rect = title_surface.get_rect(center=(data.window_width // 2, data.window_height // 4))
    data.window.blit(title_surface, title_rect)

    # Show the current level and score (bold and larger)
    level_text = f"Level {level}"
    level_surface = font_bold.render(level_text, True, Color.WHITE)
    level_rect = level_surface.get_rect(center=(data.window_width // 2, data.window_height // 3))
    data.window.blit(level_surface, level_rect)

    # Display next level and main menu messages (bold and larger)
    next_level_text = "Press Enter to Proceed to Next Level"
    next_level_surface = font_bold.render(next_level_text, True, Color.WHITE)
    next_level_rect = next_level_surface.get_rect(center=(data.window_width // 2, data.window_height // 1.5))
    data.window.blit(next_level_surface, next_level_rect)

    main_menu_text = "Press Escape to Return to Main Menu"
    main_menu_surface = font_bold.render(main_menu_text, True, Color.WHITE)
    main_menu_rect = main_menu_surface.get_rect(center=(data.window_width // 2, data.window_height // 1.3))
    data.window.blit(main_menu_surface, main_menu_rect)
    
    if data.game_input.enter:
        data.current_screen = screen.game

    # Refresh the display
    pygame.display.flip()

    # Event handling loop for the Enter and Escape keys
    
