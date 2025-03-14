import pygame
from src import data
from src.color import Color
from src.enums import screen

# Global variables for the level and score
level = 1  # Example initial level
score = 0  # Example initial score

# Font: Increased size and set to bold
font = pygame.font.SysFont("comic sans", 72)  # 72px font size, adjust as needed
font_bold = pygame.font.SysFont("comic sans", 72)
font_title = pygame.font.SysFont("Comic sans", 150)# Bold font, same size

# Set the font to bold
font_bold.set_bold(True)

def home(player1, player2, world):
    """
    Displays the home screen with the title "Pype Flip" and an option to proceed.
    This version doesn't require arguments, using global variables for level and score.
    """
    # Load and display the background image first
    try:
        background_image = pygame.image.load('./assets/img/home.jpg')
        background_image = pygame.transform.scale(background_image, (data.window_width, data.window_height))
        data.window.blit(background_image, (0, 0))
    except pygame.error as e:
        print(f"Error loading image: {e}")

    # Display the big title text: "Pype Flip"
    title_text = "PYpe Flip"
    title_surface = font_title.render(title_text, True, Color.BLACK)  # Change Color.WHITE for better contrast
    title_rect = title_surface.get_rect(center=(data.window_width // 2, data.window_height // 4))
    data.window.blit(title_surface, title_rect)

    # Display the "Press Enter" message (bold and larger)
    next_level_text = "Press Enter to Proceed to Next Level"
    next_level_surface = font_bold.render(next_level_text, True, Color.WHITE)
    next_level_rect = next_level_surface.get_rect(center=(data.window_width // 2, data.window_height // 1.5))
    data.window.blit(next_level_surface, next_level_rect)


    if data.game_input.enter:
        data.current_screen = screen.game
        world.update()
        
    # Refresh the display
    pygame.display.flip()    
