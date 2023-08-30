from src.game.color import Color
from src.game.grid import GridOfGrids
from src.game.player import Player

import pygame

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
        self.door_wrap = False
        self.tile_size = 16
        self.max_x = max_x
        self.max_y = max_y
        self.player = Player(10, max_x / 2, max_y / 2, Color(0, 255, 0))
        self.gridID_x = 0
        self.gridID_y = 0

        self.input = InputState(False, False, False, False)
        self.running = False
        self.gridOfGrids = GridOfGrids(self.max_x)
        self.currentGridElement = self.gridOfGrids.get_grid(self.gridID_x, self.gridID_y)
        self.show_state = True

    def format_state(self):
        state = ""
        state += "Tile Size: {}\n".format(self.tile_size)
        state += "Grid Size X:{}, Y:{}\n".format(self.max_x, self.max_y)
        state += "Current Grid ID X:{}, Y:{}\n".format(self.gridOfGrids.x_size, self.gridOfGrids.y_size)
        state += "Player Coordinates: ({},{})\n".format(self.player.x, self.player.y)
        state += "Player Grid: ({}, {})".format(self.gridID_x, self.gridID_y)
        return state

    def generate_state_image_overlay(self, screen):
        x = 20
        y = 20
        fsize = 30
        font = pygame.font.SysFont(None, fsize, )
        state = self.format_state()

        lines = state.splitlines()
        for i, l in enumerate(lines):
            screen.blit(font.render(l, True, (200,200,200)), (x, y + fsize * i))

