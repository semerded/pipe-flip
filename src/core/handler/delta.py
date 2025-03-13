from src import data
                
def calculate_delta(speed):
    """
    Calculates the movement delta based on speed and frame time.

    :param speed: The speed in units per second
    :return: The delta (adjusted movement per frame)
    """
    fps = data.clock.get_fps()
    if fps == 0.0:
        return 0
    return speed / fps