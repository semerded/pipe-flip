import pygame
from src.enums import colorBlindType
from src import data
from src.core.utils.screenunit import *
from typing import TYPE_CHECKING
from src.color import Color
from src.core.utils.rect import Rect
from src.core.handler.delta import calculate_delta
from src.game.tile import Tile
from src.core.handler.sound import SoundManager

if TYPE_CHECKING:
    from src.game.input import Input


class Player:
    def __init__(self, input: 'Input', img: str, upside_down: bool, player_number: int):
        self.color_blind_type = colorBlindType.none

        # object of sounmanager
        self.sound_manager = SoundManager()
         # To track if the jump sound has played
        self.jumped = False 

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

        # movemvent speed

        self.X_SPEED = 300
        self.Y_UP_SPEED = 600
        self.Y_DOWN_SPEED = 700


    def change_chunk(self):
        self.upside_down = not self.upside_down
        self.img = pygame.transform.flip(self.img, False, self.upside_down)

    def cycle(self, tile_grid) -> bool:
        """
        main cycle of the player\n
        returns true if staged an update
        """
        self.move(tile_grid)

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

    def get_nearby_tile_indices(self, tile_list):
        """
        Returns indices of tiles in tile_list whose .rect collides with the player's rect.
        This uses the built-in collidelistall method.
        """
        # Build the list of tile rects.
        tile_rects = [tile.rect for tile in tile_list]
        # collidelistall returns a list of indices where collisions occur.
        return self.rect.collidelistall(tile_rects)
        
    def get_nearby_tiles(self, tile_list):
        indices = self.get_nearby_tile_indices(tile_list)
        return [tile_list[i] for i in indices]  


    def move(self, tile_grid):
        """
        Moves the player's position and resolves collisions with tiles by updating
        self.x and self.y. This method assumes that collisions are resolved along the
        horizontal axis first, then the vertical axis.
        """
        # Save the old collision rectangle.
        self.previous_rect = self.rect

        horizontal_move = 0
        prev_x = self.x

        # --- Horizontal movement ---
        if self.input.player_is_moving_left(self.player_number):
            self.x -= calculate_delta(self.X_SPEED)
            horizontal_move += 1
            self.stage_update = True

        if self.input.player_is_moving_right(self.player_number):
            self.x += calculate_delta(self.X_SPEED)
            horizontal_move += 2
            self.stage_update = True

        if horizontal_move == 3:
            # Both directions pressed; cancel horizontal movement.
            self.x = prev_x
            horizontal_move = 0

        # Play footsteps sound only if moving left or right, but not both at once
        if horizontal_move in [1, 2]:  # 1 = left, 2 = right
            self.sound_manager.play_sound("footsteps")

        # Update the collision rectangle (for horizontal movement).
        self.rect = self.get_rect()

        if horizontal_move > 0:
            nearby_tiles = self.get_nearby_tiles(tile_grid)
            for tile in nearby_tiles:
                if self.rect.colliderect(tile.rect):
                    if horizontal_move == 2:  # Moving right.
                        self.rect.right = tile.rect.left
                    elif horizontal_move == 1:  # Moving left.
                        self.rect.left = tile.rect.right
            # Update self.x to follow the resolved collision.
            self.x = self.rect.x

        # --- Vertical movement ---
        if self.input.player_is_jumping(self.player_number):
            if not self.jump_action:
                self.ground_pos = self.y
                self.jump_action = True
                # When jumping, set the threshold (taking into account inversion).
                self.jump_threshold = self.y - self._factor_upside_down(self.img.get_height()) * self.jump_height
                self.jumping_up = True

        if self.jump_action:
            self._jump()  # This updates self.y accordingly.
            self.stage_update = True

        # Update collision rectangle after vertical movement.
        self.rect = self.get_rect()

        # Resolve vertical collisions.
        nearby_tiles = self.get_nearby_tiles(tile_grid)
        for tile in nearby_tiles:
            if self.rect.colliderect(tile.rect):
                if not self.jumping_up:
                    # Moving down: snap player's bottom to tile's top.
                    self.rect.bottom = tile.rect.top
                elif self.jumping_up:
                    # Moving up: snap player's top to tile's bottom.
                    self.rect.top = tile.rect.bottom
        # Update self.y to reflect the resolution.
        self.y = self.rect.y

        # Recalculate the collision rectangle to have the final position.
        self.rect = self.get_rect()


    
    def _jump(self):
        if self.jumping_up:
            # Trigger jump sound when jumping up
            if not self.jumped:
                # Assuming 'jump' is the key for the jump sound in your SoundManager
                self.sound_manager.play_sound("jump")  
                # Make sure the sound only plays once per jump
                self.jumped = True  

            self.y -= self._factor_upside_down(calculate_delta(600))
            if (not self.upside_down and self.y <= self.jump_threshold) or (self.upside_down and self.y >= self.jump_threshold):
                self.jumping_up = False
        else:
            self.y += self._factor_upside_down(calculate_delta(700))
            if (not self.upside_down and self.y >= self.ground_pos) or (self.upside_down and self.y <= self.ground_pos):
                self.y = self.ground_pos
                self.jump_action = False
                # Reset the flag when the player lands
                self.jumped = False  


    def _factor_upside_down(self, value):
        return value * -1 if self.upside_down else value

    def get_rect(self) -> Rect:
        return Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
