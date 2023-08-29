import pygame
import logging

from src.game.state import Context


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
            currentGrid.get_grid_tile(bottom_right[0], bottom_right[1])]:
            tile_action = tile.action()


            if tile_action.type == "Collide":
                action = tile_action
                break
            elif tile_action.type == "Door":
                action = tile_action
                break
            elif tile_action.type == "Air":
                action = tile_action
            else:
                logging.error(tile_action)

        match action:
            case ("Door", _):
                logging.info("door")
                match action:
                    case ("Door", "up"):
                        logging.error("door up")
                    case("Door", "down"):
                        logging.error("door down")
                    case ("Door", "left"):
                        logging.error("door left")
                    case ("Door", "right"):
                        logging.error("door right")
                    case _:
                        logging.error("door has no direction")
            case ("Air", _):
                logging.info("air")
                self.context.player.move_player(x, y)
            case _ :
                pass


