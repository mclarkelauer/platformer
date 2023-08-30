from math import floor
from collections import namedtuple
import pygame
from enum import Enum

from src.game.color import Color

class BlockType(Enum):
    AIR = 1
    DOOR = 2
    SOLID = 3

GridID = namedtuple("GridID", "x y")
Coordinate = namedtuple("Coordinate", "x y")
Action = namedtuple("Action", "type action")

class GridBlock():
    def __init__(self, color):
        self.color = color
        self.block_type = BlockType.AIR

    def action(self):
        return Action("Air", None)

    def get_block_type(self):
        return self.block_type

AirBlock = GridBlock(Color(0,0,0))

class SolidBlock(GridBlock):
    def __init__(self):
        super().__init__(Color(255,0,0))
        self.block_type = BlockType.SOLID

    def action(self):
        return Action('Collide', None)

class Door(GridBlock):
    def __init__(self, target_grid, target_coordinate):
        super().__init__(Color(255,255,255))
        self.target_grid = target_grid
        self.target_coordinate = target_coordinate
        self.block_type = BlockType.DOOR

    def action(self):
        return Action("Door", {"grid":self.target_grid, "coordinates":self.target_coordinate})

WallBlock=SolidBlock()

class GridScreen():
    def __init__(self, grid_size,screen_size):
        self.grid_size = grid_size
        self.grid = []
        self.tile_size = screen_size/self.grid_size

    def draw_grid(self, screen):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                pygame.draw.rect(screen, self.grid[i][j].color, pygame.Rect(
                    i*self.tile_size, j*self.tile_size, (i+1)*self.tile_size, (j+1)*self.tile_size))

    def get_grid_tile(self,x,y):
        # TODO - detect edges here since we are already doing the location check
        # TODO - remove execption handling as control flow.... this is gross and i am ashamed
        try:
            tile_x = floor(x/self.tile_size)
            tile_y = floor(y/self.tile_size)
            return self.grid[int(tile_x)][int(tile_y)]
        except IndexError:
            return None


class DefaultGridScreen(GridScreen):
    def __init__(self, grid_size, screen_size):
        super().__init__(grid_size, screen_size)
        self.grid = []
        for i in range(grid_size):
            self.grid.append([])
            for j in range(grid_size):
                if i == 0 or i == grid_size-1 or j == 0 or j == grid_size-1:
                    self.grid[i].append(WallBlock)
                else:
                    self.grid[i].append(AirBlock)

                if j == grid_size-1 and i >= 20 and i <= 40:
                    self.grid[i][j] = AirBlock

                if j == 0 and i >= 20 and i <= 40:
                    self.grid[i][j] = AirBlock

                if i == grid_size - 1 and j >= 20 and j <= 40:
                    self.grid[i][j] = AirBlock

                if i == 0 and j >= 20 and j <= 40:
                    self.grid[i][j] = AirBlock


class GridOfGrids():
    def __init__(self, screen_size):
        self._griddie = [[DefaultGridScreen(64,screen_size),DefaultGridScreen(64,screen_size)],
                         [DefaultGridScreen(64,screen_size), DefaultGridScreen(64,screen_size)]]

        self._griddie[0][0].grid[45][45]= Door(GridID(1,1), Coordinate(320,320))
        self.x_size = 2
        self.y_size = 2

    def get_grid(self, x, y):
        return self._griddie[y][x]