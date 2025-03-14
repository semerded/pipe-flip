import pygame
import numpy as np


COLORBLIND_MATRICES = {
    "protanopia": np.array([[0.567, 0.433, 0], [0.558, 0.442, 0], [0, 0.242, 0.758]]),
    "deuteranopia": np.array([[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.3, 0.7]]),
    "tritanopia": np.array([[0.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, 0.525]])
}

def apply_colorblind_filter(surface, mode):
    """Applies a color transformation to simulate colorblindness."""
    matrix = COLORBLIND_MATRICES.get(mode, np.eye(3))
    array = pygame.surfarray.array3d(surface)

    # Apply transformation
    transformed_array = np.dot(array, matrix.T)
    transformed_array = np.clip(transformed_array, 0, 255).astype(np.uint8)

    return pygame.surfarray.make_surface(transformed_array)
