import click

from game.game import Game


@click.option('--y', default=640, help='Max X dimension')
@click.option('--x', default=480, help='Max Y dimension')
@click.command()
def run_game(x, y):
    game_instance = Game(x, y)
    game_instance.run_game()


if __name__ == "__main__":
    run_game()
