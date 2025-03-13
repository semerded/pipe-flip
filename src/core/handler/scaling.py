from src import data

class Scaling:
    @staticmethod
    def tile_to_screenunit(tile: int) -> int:
        return tile * data.TILE_SIZE
    
    @staticmethod
    def screenunit_to_tile(screenunit: int) -> int:
        return int(screenunit // data.TILE_SIZE) + (1 if screenunit % data.TILE_SIZE != 0 else 0)
    
