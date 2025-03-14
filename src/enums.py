from enum import Enum

class colorBlindType(Enum):
    none = ""
    protanopia = "protanopia"
    deuteranopia = "deuteranopia"
    tritanopia = "tritanopia"
    
    
class screen(Enum):
    intro = 0
    game = 1
    menu = 2
    
    game_over = 3
    level_finished = 4
    home = 5
 
    