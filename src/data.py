import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.utils.camera import Camera
    
# Display information
display_info = pygame.display.Info()
display_width: int = display_info.current_w
display_height: int = display_info.current_h

window_width: int = 800
window_height: int = 600
window: pygame.Surface = None

camera: 'Camera' = None

game_running: bool = True
