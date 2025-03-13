import pygame
from src.color import Color
from src.core.utils.rect import Rect
from src import data


class Text:
    anti_alias: bool = True
    text_rect: Rect = Rect(0, 0, 0, 0)

    def __init__(self, text, font, color, bold=False, italic=False):
        self.text = text
        self.font: pygame.font.Font = font
        self.color = color

        self.bg_color = None

        self.font.bold = bold
        self.font.italic = italic
        self._render_text(self.text)

    def set_anti_alias(self, active):
        self.anti_alias = active
        self._render_text(self.text)

    def set_text_color(self, color):
        self.color = color
        self._render_text(self.text)

    def set_background_color(self, color):
        self.bg_color = color
        self._render_text(self.text)

    def set_text(self, text, bold=False, italic=False):
        self.text = text
        self.font.bold = bold
        self.font.italic = italic
        self._render_text(text)

    def _render_text(self, text):
        self.text_surface = self.font.render(
            text, self.anti_alias, self.color, self.bg_color)
        self.height = self.text_surface.get_height()
        self.width = self.text_surface.get_width()

    def draw(self, x, y):
        self.text_rect = Rect(x, y, self.width, self.height)
        data.window.blit(self.text_surface, (x, y))

    def place_in_rect(self, rect, percent_x, percent_y):
        _rect: Rect = rect
        x = _rect.x + (_rect.w - self.width) * percent_x
        y = _rect.y + (_rect.h - self.height) * percent_y
        self.text_rect = Rect(x, y, self.width, self.height)
        data.window.blit(self.text_surface, (x, y))

    @property
    def get_rect(self):
        return self.text_rect
