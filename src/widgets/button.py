import pygame
from src.color import Color
from src.core.utils.rect import Rect
from src import data
from src.widgets.text import Text
from time import time

class Button:
    pressing_time = 0
    double_click_time_difference = 0
    double_click_max_interval = 0.5  # seconds (default on Windows)

    def __init__(self, x, y, width, height, color, border_radius=-1) -> None:
        self.text = None
        self.color = color
        self.border_radius = border_radius
        self.rect = Rect(x, y, width, height)
    
    def set_text(self, text, font, color, bold=False, italic=False):
        self.text = Text(text, font, color, bold, italic)
            
    def is_held_for(self, milliseconds: int):
        if data.game_input.is_mouse_clicked_in_rect(self.rect):
            self.pressing_time = time()
        
        if data.game_input.is_mouse_clicked_in_rect(self.rect) and (time() - self.pressing_time > milliseconds / 1000):
            return True
        return False
    
    def is_double_clicked(self):
        if data.game_input.is_mouse_clicked_in_rect(self.rect):
            if time() - self.double_click_time_difference < self.double_click_max_interval:
                self.double_click_time_difference = 0
                return True
            self.double_click_time_difference = time()
        if data.game_input.is_mouse_clicked_outside_rect(self.rect):
            self.double_click_time_difference = 0
        return False 
    
    def is_clicked(self):
        return data.game_input.is_mouse_clicked_in_rect(self.rect)
    
    def is_pressed(self):
        return data.game_input.is_mouse_pressing_in_rect(self.rect)

    def is_released(self):
        return data.game_input.is_mouse_released_in_rect(self.rect)
    
    def draw(self):
        pygame.draw.rect(data.window, self.color, self.rect.pack(), 0, self.border_radius)
        if self.text is not None:
            self.text.draw(self.rect.x + self.rect.w / 2 - self.text.width / 2, self.rect.y + self.rect.h / 2 - self.text.height / 2)

    @property       
    def get_pressing_time(self):
        return self.pressing_time
        
