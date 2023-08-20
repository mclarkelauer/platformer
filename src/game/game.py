import pygame

from src.game.color import Color
from src.game.grid import GridOfGrids


class Player():
    def __init__(self, size, x, y, color):
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.step_size = 1

    def draw(self,screen):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.size)

    def compute_player_move(self, input):
        x = self.x
        y = self.y
        step = self.step_size
        if input.is_diag():
            step *= .75
        if input.up:
            y -= step
        if input.down:
            y += step
        if input.left:
            x -= step
        if input.right:
            x += step
        return x,y

    def move_player(self, x , y):
        self.x = x
        self.y = y

    def get_player_boundaries(self, x = None, y = None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        return (x-self.size, y-self.size, x+self.size, y+self.size)

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
        self.player = Player(10, max_x / 2, max_y / 2, Color(0, 255, 0))
        self.gridID = {'x': 0, 'y': 0}
        self.input = InputState(False, False, False, False)
        self.running = False
        self.gridOfGrids = GridOfGrids(self.max_x)
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
            self.screen)
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
        currentGrid = self.context.currentGridElement
        input = self.context.input
        # detect overlap
        (x , y) = self.context.player.compute_player_move(input)
        min_x, min_y, max_x, max_y = self.context.player.get_player_boundaries(x,y)

        # detect edge collision with grid
        top_left = min_x, min_y
        top_right = max_x, min_y
        bottom_left = min_x, max_y
        bottom_right = max_x, max_y

        action = None
        for tile in [
            currentGrid.get_grid_tile(top_left[0], top_left[1]),
            currentGrid.get_grid_tile(top_right[0], top_right[1]),
            currentGrid.get_grid_tile(bottom_left[0], bottom_left[1]),
            currentGrid.get_grid_tile(bottom_right[0], bottom_right[1]),
        ]:
            print("collision")
        else:
            self.context.player.move_player(x, y)
