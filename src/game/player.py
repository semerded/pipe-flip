import pygame
from src.enums import colorBlindType
from src import data
from src.core.utils.screenunit import *
from typing import TYPE_CHECKING
from src.color import Color
from src.core.utils.rect import Rect
from src.core.handler.delta import calculate_delta
from src.game.tile import Tile

if TYPE_CHECKING:
    from src.game.input import Input


class Player:
    def __init__(self, input: 'Input', img: str, upside_down: bool, player_number: int):
        self.color_blind_type = colorBlindType.none

        self.player_number = player_number
        self.score = 0
        self.upside_down = upside_down

        _py_img = pygame.image.load(img)
        aspect_ratio = _py_img.get_height() / _py_img.get_width()
        _py_img = pygame.transform.smoothscale(
            _py_img, ((data.TILE_SIZE) - 2, int((data.TILE_SIZE) * aspect_ratio) - 2))
        self.img: pygame.Surface = pygame.transform.flip(
            _py_img, False, upside_down)

        self.input = input

        self.x = 20
        if self.upside_down:
            self.y = (center_of_screen()[1] + 50)
        else:
            self.y = (center_of_screen()[1] - self.img.get_height()) - 50

        # jumping variables
        self.jump_height = 2
        self.jump_action = False  # determins if the player is jumping or not
        self.ground_pos = self.y
        self.jumping_up = False
        self.jump_threshold = self.y + self.img.get_height()

        self.rect: Rect = self.get_rect()
        self.previous_rect: Rect = Rect.place_holder()
        self.stage_update: bool = True

    def change_chunk(self):
        self.upside_down = not self.upside_down
        self.img = pygame.transform.flip(self.img, False, self.upside_down)
        
    def cycle(self) -> bool:
        """
        main cycle of the player\n
        returns true if staged an update
        """
        self.move()
        
        if self.stage_update:
            self.update()
            return True
        return False
    
    def update(self):
        data.rect_update_list.append(self.rect.union(self.previous_rect))
        self.stage_update = False

    def draw(self):
        data.window.blit(self.img, (self.x, self.y))
        pygame.draw.rect(data.window, Color.GREEN, self.rect, 1)
        
    def check_collision(self, tiles: Tile):
        collision_indices  = self.rect.collidelistall(tiles)
        
        

    def move(self):
        self.previous_rect = self.rect
        if self.input.player_is_moving_left(self.player_number):
            self.x -= calculate_delta(300)
            self.stage_update = True
        elif self.input.player_is_moving_right(self.player_number):
            self.x += calculate_delta(300)
            self.stage_update = True
        if self.input.player_is_jumping(self.player_number):
            if not self.jump_action:
                self.ground_pos = self.y
                self.jump_action = True
                self.jump_threshold = self.y - \
                    self._factor_upside_down(self.img.get_height()) * self.jump_height
                self.jumping_up = True

        if self.jump_action:
            self._jump()
            self.stage_update = True
            
            
        self.rect = self.get_rect()
            
        

    def _jump(self):
        if self.jumping_up:
            self.y -= self._factor_upside_down(calculate_delta(600))
            if (not self.upside_down and self.y <= self.jump_threshold) or (self.upside_down and self.y >= self.jump_threshold):
                self.jumping_up = False
        else:
            self.y += self._factor_upside_down(calculate_delta(700))
            if (not self.upside_down and self.y >= self.ground_pos) or (self.upside_down and self.y <= self.ground_pos):
                self.y = self.ground_pos
                self.jump_action = False

    def _factor_upside_down(self, value):
        return value * -1 if self.upside_down else value

    def get_rect(self) -> Rect:
        return Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
    