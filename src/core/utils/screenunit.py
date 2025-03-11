from src import data

def dw(screen_unit: float) -> float:
    """
    display width
    """
    return data.display_width / 100 * screen_unit

def dh(screen_unit: float) -> float:
    """
    display height
    """
    return data.display_height / 100 * screen_unit

def vw(screen_unit: float) -> float:
    """
    view width 
    """
    return data.window_width / 100 * screen_unit

def vh(screen_unit: float) -> float:
    """
    view height
    """
    return data.window_height / 100 * screen_unit

def px(screen_unit: float) -> float:
    return screen_unit

def get_vw_from_pixel(pixel_x: int) -> (int | float):
    return pixel_x / (data.window_width / 100)

def get_vh_from_pixel(pixel_y: int) -> (int | float):
    return pixel_y / (data.window_height / 100)

def get_relative_position(coordinate: tuple[int]) -> tuple[(int | float)]:
    vw = get_vw_from_pixel(coordinate[0])
    vh = get_vh_from_pixel(coordinate[1])
    return vw, vh

def center_of_screen():
    return data.window_width / 2, data.window_height / 2

def center_rect_in_screen(rect_width, rect_height): 
        
    screen_center_w, screen_center_h = center_of_screen()
    return screen_center_w - (rect_width / 2), screen_center_h - (rect_height / 2) 

