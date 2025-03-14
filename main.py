import os
import pygame

# init pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("pipe flip!")

# import scripts
from src import data
from src.widgets.button import Button
from src.core.handler.scaling import Scaling
from src.game.player import Player
from src.core.handler.event import event_handler
from src.game.input import Input
from src.color import Color
from src.game.world import World
from src.core.utils.camera import Camera
from src.core.handler.sound import SoundManager

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialize Pygame and SoundManager
sound_manager = SoundManager()

# Set background music to loop
sound_manager.play_background_music()


data.window = pygame.display.set_mode(
    (data.window_width, data.window_height), pygame.HWSURFACE | pygame.DOUBLEBUF)
data.camera = Camera(data.window_width, data.window_height)

data.game_input = Input()

data.clock = pygame.time.Clock()

player1 = Player(data.game_input, "assets/img/actor/player.png", False, 0)
player2 = Player(data.game_input, "assets/img/actor/player.png", True, 1)

world: World = World(player1, player2)
world.update()

from src.screen.intro import intro
from src.screen.menu import menu
from src.screen.game import game
from src.screen.game_over import game_over

screen_funcs = ((intro, ()), (game, (world, )), (menu, ()), (game_over, ()))

while data.game_running:
    # print(data.clock.get_fps())
    data.clock.tick(data.FPS)
    # data.window.fill(Color.BLACK)
    event_handler(pygame.event.get())

    current_screen_func = screen_funcs[data.current_screen.value]

    current_screen_func[0](*current_screen_func[1])
   

# Stop all sounds when game ends
sound_manager.stop_all_sounds()

# cleanup
exit(0)
