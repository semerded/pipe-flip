import pygame



class Rect(pygame.Rect):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)
        
    @classmethod
    def from_circle(cls, center, radius: int) -> 'Rect':
        return cls(center[0] - radius, center[1] - radius, radius * 2, radius * 2)
    
    @classmethod    
    def from_polygon(cls, points) -> "Rect":
        if not points:
            raise ValueError("Points list cannot be empty")
        
        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)

        return cls(min_x, min_y, max_x - min_x, max_y - min_y)
    
    def pack(self) -> 'Rect':
        """
        returns a new rect instance from a rect instance
        """
        return self

    def unpack(self):
        """
        unpacks a rect instance into a tuple (x, y, w, h)
        """
        return self.x, self.y, self.w, self.h

    def rw(self, screen_unit):
        """
        a rect's relative width\n
        ```
        rect = Rect(100, 200, 400, 150) # x, y, w, h
        print(rect.rw(50)) # = 200
        print(rect.rw(80)) # = 320
        ```
        """
        return self.w / 100 * screen_unit

    def rh(self, screen_unit):
        """
        a rect's relative height\n
        ```
        rect = Rect(100, 200, 400, 150) # x, y, w, h
        print(rect.rh(50)) # = 75
        print(rect.rh(80)) # = 120
        ```
        """
        return self.h / 100 * screen_unit
    
    def aw(self, screen_unit):
        """
        a rect's absolute width\n
        ```
        rect = Rect(100, 200, 400, 150) # x, y, w, h
        print(rect.aw(50)) # = 300
        print(rect.aw(80)) # = 420
        ```
        """
        return self.rw(screen_unit) + self.x
    
    def ah(self, screen_unit):
        """
        a rect's absolute height\n
        ```
        rect = Rect(100, 200, 400, 150) # x, y, w, h
        print(rect.ah(50)) # = 275
        print(rect.ah(80)) # = 320
        ```
        """
        return self.rh(screen_unit) + self.h
    
    def expand_width(self, expansion: int) -> None:
        self.w += expansion
        self.x -= int(expansion / 2)
        
    def shrink_width(self, shrinkage: int) -> None:
        self.expand_width(-shrinkage)
        
    def expand_height(self, expansion: int) -> None:
        self.h += expansion
        self.y -= int(expansion / 2)
        
    def shrink_height(self, shrinkage: int) -> None:
        self.expand_height(-shrinkage)
        
    def resize(self, width, height):
        self.w = width
        self.h = height
        
    def reposition(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def place_holder() -> "Rect":
        return Rect(0, 0, 0, 0)
