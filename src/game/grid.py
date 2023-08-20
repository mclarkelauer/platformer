from math import floor

import pygame

from src.game.color import Color

EMPTY = Color(0,0,0)
BLOCK = Color(255, 0, 0)


class GridScreen():
    def __init__(self, grid_size,screen_size):
        self.grid_size = grid_size
        self.grid = []
        self.tile_size = screen_size/self.grid_size

    def draw_grid(self, screen):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                pygame.draw.rect(screen, self.grid[i][j], pygame.Rect(
                    i*self.tile_size, j*self.tile_size, (i+1)*self.tile_size, (j+1)*self.tile_size))

    def get_grid_tile(self,x,y):
        tile_x = floor(x/self.tile_size)
        tile_y = floor(y/self.tile_size)
        return self.grid[int(tile_x)][int(tile_y)]

#adding random comment
class DefaultGridScreen(GridScreen):
    def __init__(self, grid_size, screen_size):
        super().__init__(grid_size, screen_size)
        self.grid = []
        for i in range(grid_size):
            self.grid.append([])
            for j in range(grid_size):
                if i == 0 or i == grid_size-1 or j == 0 or j == grid_size-1:
                    self.grid[i].append(BLOCK)
                else:
                    self.grid[i].append(EMPTY)


class GridOfGrids():
    def __init__(self, screen_size):
        self._griddie = [[DefaultGridScreen(64,screen_size)]]

    def get_grid(self, x, y):
        return self._griddie[y][x]
