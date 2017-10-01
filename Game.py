import click

from Round import Round

NUMBER_CARDS = 60


class Game:
    def __init__(self):
        self.players = []

    def start(self):
        number_rounds = int(NUMBER_CARDS / len(self.players))
        for round_number in range(1, number_rounds + 1):
            round_ = Round()
            round_.round_number = round_number
            round_.players = self.players
            round_.play_round()
        self.determine_winners()

    def add_player(self, player):
        self.players.append(player)

    def determine_winners(self):
        winners_value = sorted(self.players, key=lambda x: x.value)[-1]
        for p in filter(lambda x: x.value == winners_value, self.players):
            click.echo(click.style("%s you're the fucking man!" % p.name, fg='black', bold='black'))
