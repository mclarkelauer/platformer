import pygame
from collections import namedtuple
from pprint import pprint
Color = namedtuple("Color", "red green blue")

EMPTY = Color(0,0,0)
BLOCK = Color(255, 0, 0)


class GridScreen():
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = []

    def draw_grid(self, screen, screen_size):
        tile_size = screen_size/self.grid_size
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                pygame.draw.rect(screen, self.grid[i][j], pygame.Rect(
                    i*tile_size, j*tile_size, (i+1)*tile_size, (j+1)*tile_size))


class DefaultGridScreen(GridScreen):
    def __init__(self, grid_size):
        super().__init__(grid_size)
        self.grid = []
        for i in range(grid_size):
            self.grid.append([])
            for j in range(grid_size):
                if i == 0 or i == grid_size-1 or j == 0 or j == grid_size-1:
                    self.grid[i].append(BLOCK)
                else:
                    self.grid[i].append(EMPTY)


class GridOfGrids():
    def __init__(self):
        self._griddie = [[DefaultGridScreen(64)]]

    def get_grid(self, x, y):
        return self._griddie[y][x]

class Player():
    def __init__(self, size, x, y, color):
        self.size = size
        self.x = x
        self.y = y
        self.color = color

    def draw(self,screen):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.size)


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
        self.tile_size = 16
        self.max_x = max_x
        self.max_y = max_y
        self.player = Player(10, max_x/2, max_y/2, Color(0,255,0))
        self.gridID = {'x': 0, 'y': 0}
        self.input = InputState(False, False, False, False)
        self.running = False
        self.gridOfGrids = GridOfGrids()
        self.currentGridElement = self.gridOfGrids.get_grid(
            self.gridID['x'], self.gridID['y'])


class Game():
    def __init__(self, max_x, max_y):
        self.context = Context(max_x, max_y)
        self.screen = None

    def run_game(self):
        # pygame init

        pygame.init()
        self.running = True

        # Set the size of the display screen
        screen_size = (self.context.max_x, self.context.max_y)

        self.screen = pygame.display.set_mode(screen_size)
        while self.running:
            self._game_tick()
        # pygame exit
        pygame.quit()

    def _game_tick(self):
        # runs once for every game tick
        pygame.time.delay(1)
        self._process_input()
        self._update_state()
        self._draw_screen()

    def _draw_screen(self):
        # redraw scene based on new input state

        # Clear the screen
        self.screen.fill((0, 0, 0))
        self.context.currentGridElement.draw_grid(
            self.screen, self.context.max_x)
        # Draw something on the screena
        self.context.player.draw(self.screen)

        # Update the display
        pygame.display.flip()

    def _process_input(self):
        # case statement tracking input state
        # Check for events
        for event in pygame.event.get():
            # If the user quits, exit the loop
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.context.input.left = True
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.context.input.right = True
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.context.input.up = True
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.context.input.down = True

                if event.key == ord('q'):
                    self.running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.context.input.left = False
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.context.input.right = False
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.context.input.up = False
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.context.input.down = False

    def _update_state(self):
        # take input state and update game state
        step = 8

        if self.context.input.is_diag():
            step *= .75
        if self.context.input.up:
            self.context.player.y -= step
        if self.context.input.down:
            self.context.player.y += step
        if self.context.input.left:
            self.context.player.x -= step
        if self.context.input.right:
            self.context.player.x += step
