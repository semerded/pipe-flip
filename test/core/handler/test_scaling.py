import pytest

class MockData:
    TILE_SIZE = 32  

class Scaling:
    @staticmethod
    def tile_to_screenunit(tile: int) -> int:
        return tile * MockData.TILE_SIZE

    @staticmethod
    def screenunit_to_tile(screenunit: int) -> int:
        return int(screenunit // MockData.TILE_SIZE) + (1 if screenunit % MockData.TILE_SIZE != 0 else 0)

@pytest.mark.parametrize("tile, expected_screenunit", [(5, 160), (0, 0), (2, 64)])
def test_tile_to_screenunit(tile, expected_screenunit):
    assert expected_screenunit == Scaling.tile_to_screenunit(tile)

@pytest.mark.parametrize("screenunit, expected_tile", [(130, 5), (0, 0), (64, 2)])
def test_screenunit_to_tile(screenunit, expected_tile):
    assert expected_tile == Scaling.screenunit_to_tile(screenunit)
