import pygame
from src import data
from src.core.utils.rect import Rect
from src.core.handler.scaling import Scaling
from src.color import Color
from src.core.utils.screenunit import vh


class Tile:
    def __init__(self, x: int, y: int, type: str, upside_down: bool = False):
        self.upside_down = upside_down
        self.size = data.TILE_SIZE
        self.tile_x = x
        if not self.upside_down:
            self.tile_y = y
        else:
            self.tile_y = data.TILE_COUNT_Y - y - 1

        self.interactable_rect = None

        self.rect = Rect(Scaling.tile_to_screenunit(
            self.tile_x), Scaling.tile_to_screenunit(self.tile_y), self.size, self.size)
        self.type = type
        self.update_texture()

    def update_texture(self):
        if self.type == "block":
            if self.upside_down:
                self.texture = data.tile_texture_cache[self.type]["underworld"][0]
                self.texture = pygame.transform.flip(self.texture, False, True)
            else:
                self.texture = data.tile_texture_cache[self.type]["overworld"][0]
        else:
            type = self.type.split(":")
            if type[0] == "trap":
                if type[1] == "spikes":
                    self.texture = data.tile_texture_cache[type[0]][type[1]][0]
                    if self.upside_down:
                        self.interactable_rect = Rect(
                            self.rect.x,
                            self.rect.y,
                            self.rect.w,
                            self.rect.rh(20),
                        )
                    else:
                        self.interactable_rect = Rect(
                            self.rect.x, self.rect.y + self.rect.rh(80), self.rect.w, self.rect.rh(20),)
            elif type[0] == "door":
                pass
            elif type[0] == "button":
                if type[1] == "notpressed":
                    self.texture = data.tile_texture_cache[type[0]][type[1]][0]
                    self.interactable_rect = Rect(
                        self.rect.x, self.rect.y +
                        self.rect.rh(60), self.rect.w, self.rect.rh(40)
                    )
                elif type[1] == "pressed":
                    self.texture = data.tile_texture_cache[type[0]][type[1]][0]
                    self.interactable_rect = None
            elif type[0] == "sign":
                pass
            elif type[0] == "coin":
                pass

        if self.upside_down:
            self.texture = pygame.transform.flip(self.texture, False, True)

    def cycle(self):
        pass

    def draw(self, surface):
        if self.upside_down:
            y = self.rect.y - vh(50)
        else:
             y = self.rect.y
        surface.blit(self.texture, (self.rect.x, y))
        if self.interactable_rect is not None and data.debugging:
            pygame.draw.rect(surface, Color.RED, self.interactable_rect, 1)
