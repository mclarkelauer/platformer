import pygame
from collections import namedtuple

InputState = namedtuple("InputState", "up down left right")


class Context():
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.player_x = max_x/2
        self.player_y = max_y/2
        self.screen_id = 0
        self.input = InputState(False, False, False, False)
        self.running = False


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
        pygame.exit()

    def _game_tick(self):
        # runs once for every game tick

        self._process_input()
        self._update_state()
        self._draw_screen()

    def _draw_screen(self):
        # redraw scene based on new input state

        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Draw something on the screen
        pygame.draw.circle(self.screen, (255, 0, 0), (320, 240), 100)

        # Update the display
        pygame.display.update()

    def _process_input(self):
        # case statement tracking input state
        # Check for events
        for event in pygame.event.get():
            # If the user quits, exit the loop
            if event.type == pygame.QUIT:
                break

    def _update_state(self):
        # take input state and update game state
        pass
