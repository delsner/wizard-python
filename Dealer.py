import click

from CardDeck import CardDeck


class Dealer:

    def __init__(self, stack=None):
        self.stack = stack
        self.trump_color = ''

    def reset_card_deck(self):
        self.stack = CardDeck()

    def deal_cards(self, players=None, amount=0):
        for _ in range(amount):
            for player in players:
                player.receive_card(self.stack.draw_card())

    def determine_trump(self):
        if len(self.stack) > 0:
            self.trump_color = self.stack.draw_card().color
        return self.trump_color
