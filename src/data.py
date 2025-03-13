import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.utils.camera import Camera
    from src.game.input import Input
    from src.core.utils.rect import Rect
    
FPS: int = 60

# Display information
ASPECT_RATIO: float = 16 / 9
display_info = pygame.display.Info()
display_width: int = display_info.current_w
display_height: int = display_info.current_h

# Get smallest display size to ensure everything is visible
if display_width < display_height * ASPECT_RATIO:
    display_width = int(display_height * ASPECT_RATIO)
else:
    display_height = int(display_width / ASPECT_RATIO)
    
window_width: int = display_width
window_height: int = display_height
window: pygame.Surface = None

TILE_COUNT_X: int = 48
TILE_COUNT_Y: int = int(TILE_COUNT_X / ASPECT_RATIO)
TILE_SIZE: int = int(window_width / TILE_COUNT_X) # values should be ints with aspect ratio 16/9

rect_update_list: list['Rect'] = []

camera: 'Camera' = None

game_running: bool = True

game_input: 'Input' = None

clock: pygame.time.Clock = None
