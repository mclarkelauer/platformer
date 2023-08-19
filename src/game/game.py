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

    def run_game(self):
        # pygame init
        self.running = True

        while self.running:
            self._game_tick()
        # pygame exit

    def _game_tick(self):
        # runs once for every game tick
        self._process_input()
        self._update_state()
        self._draw_screen()
        pass

    def _draw_screen(self):
        # redraw scene based on new input state
        pass

    def _process_input(self):
        # case statement tracking input state
        pass

    def _update_state(self):
        # take input state and update game state
        pass
