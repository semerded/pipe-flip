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
from src.enums import screen

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
            self.y = (center_of_screen()[1] + vh(40))
        else:
            self.y = (center_of_screen()[1] - self.img.get_height()) - vh(40)

        # jumping variables
        self.jump_height = 3
        self.jump_action = False  # determins if the player is jumping or not
        self.ground_pos = self.y
        self.jumping_up = False
        self.jump_threshold = self.y + self.img.get_height()
        self.jump_held = False

        self.rect: Rect = self.get_rect()
        self.previous_rect: Rect = Rect.place_holder()
        self.stage_update: bool = True

        # movemvent speed

        self.X_SPEED = vw(12)
        self.Y_UP_SPEED = vh(40)
        self.Y_DOWN_SPEED = vh(50)

    def change_chunk(self):
        self.upside_down = not self.upside_down
        self.img = pygame.transform.flip(self.img, False, self.upside_down)
        
    def reset_cord(self):
        self.x = 20
        if self.upside_down:
            self.y = (center_of_screen()[1] + vh(40))
        else:
            self.y = (center_of_screen()[1] - self.img.get_height()) - vh(40)

    def cycle(self, tile_list) -> bool:
        """
        main cycle of the player\n
        returns true if staged an update
        """
        self.move(tile_list)
        
        self.check_special_tiles(tile_list)

        if self.stage_update:
            self.update()
            return True
        return False

    def update(self):
        data.rect_update_list.append(self.rect.union(self.previous_rect))
        self.stage_update = False

    def draw(self):
        data.window.blit(self.img, (self.x, self.y))

    def get_nearby_tile_indices(self, tile_list):
        """
        Returns indices of tiles in tile_list whose .rect collides with the player's rect.
        This uses the built-in collidelistall method.
        """
        # Build the list of tile rects.
        tile_rects: list[Rect] = []
        for tile in tile_list:
            if tile.type == "block":
                tile_rects.append(tile.rect)
                
        # collidelistall returns a list of indices where collisions occur.
        return self.rect.collidelistall(tile_rects)

    def get_nearby_tiles(self, tile_list):
        indices = self.get_nearby_tile_indices(tile_list)
        return [tile_list[i] for i in indices]

    def move(self, tile_list):
        """
        Moves the player's position and resolves collisions with tiles by updating
        self.x and self.y. Collision resolution is handled horizontally first and then vertically.
        Gravity and collisions are resolved differently for an upside-down player.
        """
        # Save the old collision rectangle.
        self.previous_rect = self.rect

        horizontal_move = 0
        prev_x = self.x
        just_jumped = False

        # --- Horizontal Movement ---
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

        # Update collision rectangle after horizontal changes.

        # Play footsteps sound only if moving left or right, but not both at once

        # Update the collision rectangle (for horizontal movement).

        self.rect = self.get_rect()

        if horizontal_move > 0:
            nearby_tiles = self.get_nearby_tiles(tile_list)
            for tile in nearby_tiles:
                if self.rect.colliderect(tile.rect):
                    if horizontal_move == 2:  # Moving right.
                        self.rect.right = tile.rect.left
                    elif horizontal_move == 1:  # Moving left.
                        self.rect.left = tile.rect.right
            self.x = self.rect.x

        # --- Vertical Movement ---
        # Edge-triggered jump: only initiate jump if the jump button is pressed now and wasn't already held.
        if self.input.player_is_jumping(self.player_number):
            if not self.jump_held and not self.jump_action:
                self.ground_pos = self.y
                self.jump_action = True
                self.jumping_up = True
                self.jump_threshold = self.y - \
                    self._factor_upside_down(
                        self.img.get_height()) * self.jump_height
                just_jumped = True
            # Mark jump as held so it cannot be re-triggered.
            self.jump_held = True
        else:
            # When the jump button is not pressed, clear the flag so new jumps can occur.
            self.jump_held = False

        if self.jump_action:
            self._jump()  # _jump() updates self.y based on jump speeds.
            self.stage_update = True
        else:
            # Not jumping: apply gravity.
            # For normal players, y increases (falling down). For upside-down, _factor_upside_down negates the delta (falling up).
            self.y += self._factor_upside_down(
                calculate_delta(self.Y_DOWN_SPEED))
            self.stage_update = True

        # Update collision rectangle after vertical movement.
        self.rect = self.get_rect()

        # --- Vertical Collision Resolution ---
        nearby_tiles = self.get_nearby_tiles(tile_list)
        for tile in nearby_tiles:
            if self.rect.colliderect(tile.rect):
                if self.upside_down:
                    # Upside-down player collisions.
                    if not self.jumping_up:
                        # When falling under reversed gravity (i.e. moving upward), snap the player's top to the tile's bottom.
                        self.rect.top = tile.rect.bottom
                        self.y = self.rect.y
                        self.jump_action = False  # Landed.
                    elif self.jumping_up and not just_jumped:
                        # When "jumping" (moving downward relative to screen), snap the player's bottom to the tile's top.
                        self.rect.bottom = tile.rect.top
                        self.y = self.rect.y
                        self.jumping_up = False
                else:
                    # Normal (overworld) player collisions.
                    if not self.jumping_up:
                        # When falling (moving downward), snap player's bottom to tile's top.
                        self.rect.bottom = tile.rect.top
                        self.y = self.rect.y
                        self.jump_action = False  # Landed.
                    elif self.jumping_up and not just_jumped:
                        # When jumping upward, snap player's top to tile's bottom.
                        self.rect.top = tile.rect.bottom
                        self.y = self.rect.y
                        self.jumping_up = False

        # Sync vertical position and update collision rectangle.
        self.y = self.rect.y
        self.rect = self.get_rect()

        # play sounds

        # 1 = left, 2 = right
        if horizontal_move in [1, 2] and self.x != prev_x and not self.jump_action:
            self.sound_manager.play_sound("footsteps")

        if just_jumped:
            self.sound_manager.play_sound("jump")

    def _jump(self):
        if self.jumping_up:
            # While jumping upward: normal behavior is to decrease y for an overworld player.
            self.y -= self._factor_upside_down(
                calculate_delta(self.Y_UP_SPEED))
            # Check if jump threshold is reached depending on orientation.
            if (not self.upside_down and self.y <= self.jump_threshold) or \
                    (self.upside_down and self.y >= self.jump_threshold):
                self.y -= self._factor_upside_down(
                    calculate_delta(self.Y_UP_SPEED))
            if (not self.upside_down and self.y <= self.jump_threshold) or (self.upside_down and self.y >= self.jump_threshold):
                self.jumping_up = False
        else:
            # While falling in a jump: increase y for overworld, decrease for upside-down.
            self.y += self._factor_upside_down(
                calculate_delta(self.Y_DOWN_SPEED))
            if (not self.upside_down and self.y >= self.ground_pos) or \
                    (self.upside_down and self.y <= self.ground_pos):
                self.y = self.ground_pos
                self.jump_action = False

    def _factor_upside_down(self, value):
        return value * -1 if self.upside_down else value

    def get_rect(self) -> Rect:
        return Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def check_special_tiles(self, tile_list):
        tile_rect_map = [(tile, tile.interactable_rect) for tile in tile_list if tile.interactable_rect is not None]
        rect_list = [pair[1] for pair in tile_rect_map]
        collide_indices = self.rect.collidelistall(rect_list)
        collide_tiles = [tile_rect_map[i][0] for i in collide_indices]

        for tile in collide_tiles:
            print(f"Collided with tile of type: {tile.type}")
            if tile.type == "trap:spikes":
                self.sound_manager.pause_and_play_sound("game_over", 0.5)
                data.current_screen = screen.game_over
                
            elif tile.type == "button:notpressed":
                tile.type = "button:pressed"
                tile.update_texture()
