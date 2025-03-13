import pygame
from src.game.player import Player
from src.core.utils.rect import Rect
from src.core.utils.screenunit import *
from src.color import Color
from src import data
from src.game.tile import Tile


class Chunk:
    def __init__(self, player: Player, rect: Rect, upside_down: bool):
        self.player = player
        self.rect = rect
        self.upside_down = upside_down
        
        self.TEXTURE_PATH_BASE = "assets/img/chunk/"
        self.textures: list[pygame.Surface] = []
        self.stage_update = True


        self.tiles: list[Tile] = []
        
        self._load_textures()

    def _load_textures(self):
        _type = "overworld" if not self.upside_down else "underworld"
        img = pygame.transform.scale(pygame.image.load(self.TEXTURE_PATH_BASE + _type + "1" + self.player.color_blind_type.value + ".jpg").convert(), (self.rect.width, self.rect.height))
        if self.upside_down:
            img = pygame.transform.flip(img, False, True)
        self.textures.append(img)

    def cycle(self):
        if self.player.cycle(self.tiles):
            self.draw()

    def draw(self):
        data.window.blit(self.textures[0], self.rect)
        tile: Tile
        for tile in self.tiles:
            tile.draw()
        self.player.draw()

    def update(self):
        self.player.draw()
        pygame.display.update(self.rect)
