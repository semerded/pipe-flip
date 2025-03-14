from enum import Enum

class colorBlindType(Enum):
    none = "none"
    protanopia = "protanopia"
    deuteranopia = "deuteranopia"
    tritanopia = "tritanopia"
    
    
class screen(Enum):
    intro = 0
    game = 1
    menu = 2
    game_over = 3
    