import pygame

class Input:
    def __init__(self):
        self.player_controls = [{"left": False, "right": False, "jump": False}, {"left": False, "right": False, "jump": False}]
        self.lmb_flank = False
        self.lmb_status = False
        self.enter = False
        
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
    
    def is_mouse_button_clicked(self):
        return self.lmb_flank and self.lmb_status
    
    def is_mouse_button_pressing(self):
        return self.lmb_status
    
    def is_mouse_button_released(self):
        return self.lmb_flank and not self.lmb_status
    
    def reset_mouse_button_flank(self):
        self.lmb_flank = False
    
    def is_mouse_button_in_rect(self, rect):
        return rect.collidepoint(pygame.mouse.get_pos())
        
    def is_mouse_clicked_in_rect(self, rect):
        return self.is_mouse_button_clicked() and self.is_mouse_button_in_rect(rect)
    
    def is_mouse_pressing_in_rect(self, rect):
        return self.is_mouse_button_pressing() and self.is_mouse_button_in_rect(rect)
    
    def is_mouse_released_in_rect(self, rect):
        return self.is_mouse_button_released() and self.is_mouse_button_in_rect(rect)
    
    def is_mouse_clicked_outside_rect(self, rect):
        return self.is_mouse_button_clicked() and not self.is_mouse_button_in_rect(rect)
    
    def is_mouse_pressing_outside_rect(self, rect):
        return self.is_mouse_button_pressing() and not self.is_mouse_button_in_rect(rect)
    
    def is_mouse_released_outside_rect(self, rect):
        return self.is_mouse_button_released() and not self.is_mouse_button_in_rect(rect)
    
    
    