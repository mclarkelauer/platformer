from math import floor
from collections import namedtuple
import pygame

from src.game.color import Color

Action = namedtuple("Action", "type action")

class GridBlock():
    def __init__(self, color):
        self.color = color

    def action(self):
        return Action("Air", None)

AirBlock = GridBlock(Color(0,0,0))

class SolidBlock(GridBlock):
    def __init__(self):
       super().__init__(Color(255,0,0))

    def action(self):
        return Action('Collide', None)

class Door(GridBlock):
    def __init__(self):
        super().__init__(Color(255,255,255))
        self.door_action = None

    def set_action(self, action):
        self.action = action

    def action(self):
        return Action("Door", self.door_action)

WallBlock=SolidBlock()

DownDoorBlock=Door()
DownDoorBlock.door_action = "down"

UpDoorBlock=Door()
UpDoorBlock.door_action = "up"

RightDoorBlock=Door()
RightDoorBlock.door_action = "right"

LeftDoorBlock=Door()
LeftDoorBlock.door_action = "left"

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
        tile_x = floor(x/self.tile_size)
        tile_y = floor(y/self.tile_size)
        return self.grid[int(tile_x)][int(tile_y)]


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
                    self.grid[i][j] = DownDoorBlock

                if j == 0 and i >= 20 and i <= 40:
                    self.grid[i][j] = UpDoorBlock

                if i == grid_size - 1 and j >= 20 and j <= 40:
                    self.grid[i][j] = RightDoorBlock

                if i == 0 and j >= 20 and j <= 40:
                    self.grid[i][j] = LeftDoorBlock

class GridOfGrids():
    def __init__(self, screen_size):
        self._griddie = [[DefaultGridScreen(64,screen_size)]]

    def get_grid(self, x, y):
        return self._griddie[y][x]