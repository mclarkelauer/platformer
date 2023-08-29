from src.game.color import Color
from src.game.grid import GridOfGrids
from src.game.player import Player


class InputState():
    def __init__(self, left=False, right=False, up=False, down=False):
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def is_diag(self):
        if ((self.left and self.up)
            or (self.left and self.down)
            or (self.right and self.up)
                or (self.right and self.down)):
            return True
        return False


class Context():
    def __init__(self, max_x=1024, max_y=1024, tile_size=16):
        self.door_wrap = True
        self.tile_size = 16
        self.max_x = max_x
        self.max_y = max_y
        self.player = Player(10, max_x / 2, max_y / 2, Color(0, 255, 0))
        self.gridID = {'x': 0, 'y': 0}
        self.input = InputState(False, False, False, False)
        self.running = False
        self.gridOfGrids = GridOfGrids(self.max_x)
        self.currentGridElement = self.gridOfGrids.get_grid(
            self.gridID['x'], self.gridID['y'])
