import pygame
import numpy as np
from PIL import Image

# Cache to store preprocessed full surfaces
filter_cache = {}

COLORBLIND_MATRICES = {
    "protanopia": np.array([[0.567, 0.433, 0], [0.558, 0.442, 0], [0, 0.242, 0.758]]),
    "deuteranopia": np.array([[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.3, 0.7]]),
    "tritanopia": np.array([[0.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, 0.525]]),
}

from PIL import Image
import numpy as np
import pygame

COLORBLIND_MATRICES = {
    "protanopia": np.array([[0.567, 0.433, 0], [0.558, 0.442, 0], [0, 0.242, 0.758]]),
    "deuteranopia": np.array([[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.3, 0.7]]),
    "tritanopia": np.array([[0.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, 0.525]]),
}

def apply_filter_with_pillow(surface, mode):
    matrix = COLORBLIND_MATRICES.get(mode, np.eye(3))  
    pil_image = Image.frombytes("RGB", surface.get_size(), pygame.image.tostring(surface, "RGB"))
    
    array = np.array(pil_image)
    
    transformed_array = np.dot(array[..., :3], matrix.T) 
    transformed_array = np.clip(transformed_array, 0, 255).astype(np.uint8)  
    filtered_image = Image.fromarray(transformed_array)

    return pygame.image.fromstring(filtered_image.tobytes(), filtered_image.size, filtered_image.mode)


def apply_colorblind_filter_region(surface, mode, rect):
    """
    Applies a colorblind filter to a specific rectangular region of the surface.
    """
    # Get the transformation matrix
    matrix = COLORBLIND_MATRICES.get(mode, np.eye(3))

    # Extract the region of interest (ROI) from the surface
    roi_surface = surface.subsurface(rect)
    array = pygame.surfarray.array3d(roi_surface)

    # Apply the color transformation matrix
    transformed_array = array.copy()
    transformed_array[..., 0] = array[..., 0] * matrix[0, 0] + array[..., 1] * matrix[0, 1] + array[..., 2] * matrix[0, 2]
    transformed_array[..., 1] = array[..., 0] * matrix[1, 0] + array[..., 1] * matrix[1, 1] + array[..., 2] * matrix[1, 2]
    transformed_array[..., 2] = array[..., 0] * matrix[2, 0] + array[..., 1] * matrix[2, 1] + array[..., 2] * matrix[2, 2]

    # Clip and convert back to uint8
    transformed_array = np.clip(transformed_array, 0, 255).astype(np.uint8)

    # Create a surface for the transformed region
    filtered_region_surface = pygame.surfarray.make_surface(transformed_array)

    # Blit the filtered region back to the original surface
    surface.blit(filtered_region_surface, rect.topleft)

    return surface
