import click

from game.game import Game

@click.command()
def run_game():
    game_instance = Game()
    game_instance.run()


if __name__ == "__main__":
    run_game()
