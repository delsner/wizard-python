from Card import WIZARD, JOKER


class Trick:
    def __init__(self):
        self.cards = []
        self.trump = ""

    def receive_card(self, card):
        self.cards.append(card)

    def determine_winner(self):
        winner_card = None
        for c in self.cards:
            if winner_card is None:
                winner_card = c
            elif c.value == WIZARD and winner_card.value != WIZARD:
                winner_card = c
            elif winner_card.value == JOKER and c.value == JOKER:
                pass
            elif c.value == JOKER:
                pass
            elif c.color == winner_card.color:
                winner_card = c if c.value > winner_card.value else winner_card
            elif c.color == self.trump and winner_card != self.trump:
                winner_card = c
        return self.cards.index(winner_card)
