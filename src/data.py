import pygame
from typing import TYPE_CHECKING
from src.enums import screen

if TYPE_CHECKING:
    from src.core.utils.camera import Camera
    from src.game.input import Input
    from src.core.utils.rect import Rect

FPS: int = 60

debugging: bool = False


# Display information
ASPECT_RATIO: float = 16 / 9
display_info = pygame.display.Info()
display_width: int = display_info.current_w
display_height: int = display_info.current_h

display_width = 1440

# Get smallest display size to ensure everything is visible
if display_width > display_height * ASPECT_RATIO:
    display_width = int(display_height * ASPECT_RATIO)
else:
    display_height = int(display_width / ASPECT_RATIO)

window_width: int = display_width
window_height: int = display_height
window: pygame.Surface = None

TILE_COUNT_X: int = 32
TILE_COUNT_Y: int = int(TILE_COUNT_X / ASPECT_RATIO)
# values should be ints with aspect ratio 16/9
TILE_SIZE: int = int(window_width / TILE_COUNT_X)


rect_update_list: list['Rect'] = []

camera: 'Camera' = None

game_running: bool = True

game_input: 'Input' = None

clock: pygame.time.Clock = None

current_screen: 'screen' = screen.game

current_level: int = 1

tile_texture_cache = {"block": {"overworld": [], "underworld": []}, "trap": {"spikes": []}, "button": {"notpressed": [], "pressed": []}}

tile_texture_cache["block"]["overworld"].append(pygame.transform.scale(pygame.image.load("assets/img/tile/block/overworld1.jpg"), (TILE_SIZE, TILE_SIZE)))
tile_texture_cache["block"]["underworld"].append(pygame.transform.scale(pygame.image.load("assets/img/tile/block/underworld1.jpg"), (TILE_SIZE, TILE_SIZE)))
tile_texture_cache["trap"]["spikes"].append(pygame.transform.scale(pygame.image.load("assets/img/tile/traps/spikes.png"), (TILE_SIZE, TILE_SIZE)))
tile_texture_cache["button"]["notpressed"].append(pygame.transform.scale(pygame.image.load("assets/img/tile/button/notpressed1.png"), (TILE_SIZE, TILE_SIZE)))
tile_texture_cache["button"]["pressed"].append(pygame.transform.scale(pygame.image.load("assets/img/tile/button/pressed1.png"), (TILE_SIZE, TILE_SIZE)))