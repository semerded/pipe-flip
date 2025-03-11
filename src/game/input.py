

class Input:
    def __init__(self):
        self.player_controls = [{"left": False, "right": False, "jump": False}, {"left": False, "right": False, "jump": False}]
        
    def player_left(self, player: int):
        self.player_controls[player]["left"] = True
        
    def player_right(self, palyer: int):
        self.player_controls[palyer]["right"] = True
    
    def player_jump(self, player: int):
        self.player_controls[player]["jump"] = True
        
    def player_cancel_left(self, player: int):
        self.player_controls[player]["left"] = False
        
    def player_cancel_right(self, player: int):
        self.player_controls[player]["right"] = False
        
    def player_cancel_jump(self, player: int):
        self.player_controls[player]["jump"] = False
        
    def player_is_moving_left(self, player: int):
        return self.player_controls[player]["left"]
        
    def player_is_moving_right(self, player: int):
        return self.player_controls[player]["right"]
        
    def player_is_jumping(self, player: int):
        return self.player_controls[player]["jump"]
    