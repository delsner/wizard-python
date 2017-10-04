import click

from Stack import Stack
import Trick


class Round:
    def __init__(self):
        self.stack = Stack()
        self.round_number = 0
        self.players = []
        self.trump_color = ''

    def deal_cards(self):
        for _ in range(self.round_number):
            for player in self.players:
                player.receive_card(self.stack.draw_card())
        self.determine_trump()
        click.echo(click.style(
            'Cards have been shuffled. New round with %d cards. Trump is: %s' % (self.round_number, self.trump_color),
            fg='black', bold='black'))
        click.echo(click.style('--------------------------------', fg='black', bold='black'))

    def determine_trump(self):
        if len(self.stack) > 0:
            self.trump_color = self.stack.draw_card().color

    def request_trick_guesses(self):
        for p in self.players:
            requested_tricks = p.guess_tricks()
            while not requested_tricks <= self.round_number and requested_tricks >= 0:
                requested_tricks = p.guess_tricks()
            p.guessed_tricks = requested_tricks

    def play_round(self):
        click.echo(click.style('--------------------------------', fg='black', bold='black'))
        self.deal_cards()
        self.reset_trick_guesses()
        self.request_trick_guesses()
        for _ in range(self.round_number):
            t = Trick.Trick(trump_color=self.trump_color)
            winning_player_ix = t.play_trick(self.players)
            self.players = self.players[winning_player_ix:] + self.players[:winning_player_ix]
        self.update_scores()

    def update_scores(self):
        click.echo(click.style('------------CURRENT SCORE-----------------', fg='black', bold='black'))
        for p in self.players:
            p.score += p.won_tricks
            if p.guessed_tricks == p.won_tricks:
                p.score += 5
            click.echo(click.style('%s: %d points.' % (p, p.score), fg='black', bold='black'))

    def reset_trick_guesses(self):
        for p in self.players:
            p.reset_tricks()
