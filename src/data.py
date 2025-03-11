import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.utils.camera import Camera
    from src.game.input import Input
    
# Display information
display_info = pygame.display.Info()
display_width: int = display_info.current_w
display_height: int = display_info.current_h

window_width: int = display_width
window_height: int = display_height
window: pygame.Surface = None

camera: 'Camera' = None

game_running: bool = True

game_input: 'Input' = None
