import pygame
pygame.init()
from src.core.utils.rect import Rect
from src.color import Color
from src.widgets.button import Button
import json
from src import data

width = 960
height = 640

overworld_rect = Rect(0, 0, width, (height - 100) / 2)
underworld_rect = Rect(0, (height - 100) / 2, width, (height - 100) / 2)
ASPECT_RATIO: float = 16 / 9

TILE_COUNT_X: int = 32
TILE_COUNT_Y: int = int(TILE_COUNT_X / ASPECT_RATIO)
# values should be ints with aspect ratio 16/9
TILE_SIZE: int = int(width / TILE_COUNT_X)

overwold_tile_list = []
underworld_tile_list = []
overworld_cord_list = []
underworld_cord_list = []
overworld_type_list = []
underworld_type_list = []


def tile_to_screenunit(tile: int) -> int:
    return tile * TILE_SIZE


def screenunit_to_tile(screenunit: int) -> int:
    return int(screenunit // TILE_SIZE) + (1 if screenunit % TILE_SIZE != 0 else 0)


class Tile:
    def __init__(self, x: int, y: int, type: str, color: Color):
        self.tile_x = x
        self.tile_y = y
        self.type = type
        self.color = color
        self.rect = Rect(tile_to_screenunit(self.tile_x),
                         tile_to_screenunit(self.tile_y), TILE_SIZE, TILE_SIZE)

    def draw(self):
        pygame.draw.rect(data.window, self.color, self.rect.pack())


data.window = pygame.display.set_mode((width, height))


def export(_exit=False):
    dicto = {"overworld": [], "underworld": []}
    for tile in overwold_tile_list:
        dicto["overworld"].append((tile.tile_x, tile.tile_y, tile.type))
    for tile in underworld_tile_list:
        dicto["underworld"].append(
            (tile.tile_x, tile.tile_y - TILE_COUNT_Y / 2, tile.type))
    print(json.dumps(dicto))
    if _exit:
        exit()


lmb_pressing = False
rmb_pressing = False

button_dict = {"block": Button(10, height - 90, 90, 80, Color.PINK), "sign": Button(100, height - 90, 90, 80, Color.GREEN), "door": Button(190, height - 90, 90, 80, Color.PURPLE),
               "trap:spikes": Button(280, height - 90, 90, 80, Color.GRAY), "coin": Button(370, height - 90, 90, 80, Color.SPRING_GREEN), "button:notpressed": Button(460, height - 90, 90, 80, Color.CELESTIAL_BLUE)}

button_dict["block"].set_text("Block", pygame.font.SysFont("Arial", 20), Color.BLACK)
button_dict["sign"].set_text("Sign", pygame.font.SysFont("Arial", 20), Color.BLACK)
button_dict["door"].set_text("Door", pygame.font.SysFont("Arial", 20), Color.BLACK)
button_dict["trap:spikes"].set_text("Spikes", pygame.font.SysFont("Arial", 20), Color.BLACK)
button_dict["coin"].set_text("Coin", pygame.font.SysFont("Arial", 20), Color.BLACK)
button_dict["button:notpressed"].set_text("Button", pygame.font.SysFont("Arial", 20), Color.BLACK)

active_type = "block"

def is_button_clicked(type):
    return button_dict[type].rect.collidepoint(pygame.mouse.get_pos()) and lmb_pressing

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            export(_exit=True)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                export(_exit=True)
            elif event.key == pygame.K_RETURN:
                export()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                lmb_pressing = True
            elif event.button == 3:
                rmb_pressing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                lmb_pressing = False
            elif event.button == 3:
                rmb_pressing = False

    if lmb_pressing:
        tile_x = screenunit_to_tile(event.pos[0]) - 1
        tile_y = screenunit_to_tile(event.pos[1]) - 1
        if (tile_x, tile_y) not in overworld_cord_list and (tile_x, tile_y) not in underworld_cord_list and tile_y < TILE_COUNT_Y:
            if overworld_rect.collidepoint(pygame.mouse.get_pos()):
                overwold_tile_list.append(Tile(tile_x, tile_y, active_type, button_dict[active_type].color))
                overworld_cord_list.append((tile_x, tile_y))
            else:
                underworld_tile_list.append(Tile(tile_x, tile_y, active_type, button_dict[active_type].color))
                underworld_cord_list.append((tile_x, tile_y))

    elif rmb_pressing:
        tile_x = screenunit_to_tile(event.pos[0]) - 1
        tile_y = screenunit_to_tile(event.pos[1]) - 1
        if (tile_x, tile_y) in overworld_cord_list:
            overwold_tile_list.pop(overworld_cord_list.index((tile_x, tile_y)))
            overworld_cord_list.remove((tile_x, tile_y))
        elif (tile_x, tile_y) in underworld_cord_list:
            underworld_tile_list.pop(
                underworld_cord_list.index((tile_x, tile_y)))
            underworld_cord_list.remove((tile_x, tile_y))

    if is_button_clicked("block"):
        active_type = "block"
    elif is_button_clicked("sign"):
        active_type = "sign"
    elif is_button_clicked("door"):
        active_type = "door:door"
    elif is_button_clicked("trap:spikes"):
        active_type = "trap:spikes"
    elif is_button_clicked("coin"):
        active_type = "coin"
    elif is_button_clicked("button:notpressed"):
        active_type = "button:notpressed"

    

    data.window.fill((0, 0, 0))
    pygame.draw.rect(data.window, Color.BLUE, overworld_rect.pack())
    pygame.draw.rect(data.window, Color.RED, underworld_rect.pack())
    
    for button in button_dict.values():
        button.draw()

    for tile in overwold_tile_list:
        tile.draw()
    for tile in underworld_tile_list:
        tile.draw()
    pygame.display.update()
