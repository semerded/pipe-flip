from src.widgets.text import Text
from src.widgets.button import Button
import pygame
from src import data
from src.color import Color
from src.enums import screen
from src.core.utils.screenunit import vw, vh

bg_img = pygame.transform.scale(pygame.image.load("assets/img/game_over.jpg"), (data.window_width, data.window_height))
bg_img = bg_img.convert_alpha()
bg_img.set_alpha(128)

text = Text("Game Over", pygame.font.SysFont("Comic sans", int(vw(12))), Color.REDWOOD, bold=True, italic=True)

button = Button(data.window_width / 2 - vw(20), data.window_height - vh(20), vw(40), vh(11), Color.REDWOOD, 8)
button.set_text("Try Again", pygame.font.SysFont("comic sans", int(vw(4))), Color.WHITE)


def game_over():
    data.window.fill(Color.BLACK)
    data.window.blit(bg_img, (0, 0))
    
    text.draw(data.window_width / 2 - text.width / 2, data.window_height / 2 - text.height / 2)
    button.draw()
    
    if button.is_clicked():
        data.current_screen = screen.game
    
    pygame.display.flip()