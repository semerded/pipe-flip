import pygame
from src.core.utils.rect import Rect
from src.color import Color

width = 1440
height = 910

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


def tile_to_screenunit(tile: int) -> int:
    return tile * TILE_SIZE


def screenunit_to_tile(screenunit: int) -> int:
    return int(screenunit // TILE_SIZE) + (1 if screenunit % TILE_SIZE != 0 else 0)


class Tile:
    def __init__(self, x: int, y: int):
        self.tile_x = x
        self.tile_y = y
        self.rect = Rect(tile_to_screenunit(self.tile_x),
                         tile_to_screenunit(self.tile_y), TILE_SIZE, TILE_SIZE)

        self.type = "block"

    def draw(self):
        pygame.draw.rect(window, Color.PINK, self.rect.pack())


window = pygame.display.set_mode((width, height))


def export(_exit = False):
    dicto = {"overworld": [], "underworld": []}
    for tile in overwold_tile_list:
        dicto["overworld"].append((tile.tile_x, tile.tile_y, tile.type))
    for tile in underworld_tile_list:
        dicto["underworld"].append((tile.tile_x, tile.tile_y - TILE_COUNT_Y / 2, tile.type))
    print(dicto)
    if _exit:
        exit()

lmb_pressing = False
rmb_pressing = False

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
        if (tile_x, tile_y) not in overworld_cord_list and (tile_x, tile_y) not in underworld_cord_list and tile_y < TILE_COUNT_Y * TILE_SIZE:
            if overworld_rect.collidepoint(pygame.mouse.get_pos()):
                overwold_tile_list.append(Tile(tile_x, tile_y))
                overworld_cord_list.append((tile_x, tile_y))
            else:
                underworld_tile_list.append(Tile(tile_x, tile_y))
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

    window.fill((0, 0, 0))
    pygame.draw.rect(window, Color.BLUE, overworld_rect.pack())
    pygame.draw.rect(window, Color.RED, underworld_rect.pack())

    for tile in overwold_tile_list:
        tile.draw()
    for tile in underworld_tile_list:
        tile.draw()
    pygame.display.update()
