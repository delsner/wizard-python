from Game import Game
import click

from Player import Player


def start_game():
    game = Game()
    players = click.prompt("How many players are gonna play?", type=int)

    for i in range(players):
        p = Player()
        p.name = click.prompt("Name of player %d" % (i+1), type=str)
        game.add_player(p)

    game.start()


if __name__ == "__main__":
    start_game()
