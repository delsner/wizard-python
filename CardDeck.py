from random import shuffle
from Card import Card

COLORS = ["red", "blue", "green", "yellow"]
VALUES = range(0, 15)


class CardDeck:
    def __init__(self):
        self.cards = []
        self.initialise_cards()

    def initialise_cards(self):
        for c in COLORS:
            for v in VALUES:
                card = Card()
                card.color = c
                card.value = v
                self.cards.append(card)
        shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
