from enum import Enum

class colorBlindType(Enum):
    none = ""
    protanomaly = "_protanomaly"
    deuteranomaly = "_deuteranomaly"
    tritanomaly = "_tritanomaly"
    
    
class screen(Enum):
    intro = 0
    game = 1
    menu = 2
    level_finished = 3
    home = 4
    