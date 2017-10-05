from Card import JOKER, WIZARD
import click


class Cards:
    # container of cards -> stores cards sorted
    # can create a string that represents the cards
    def __init__(self):
        self.stack = []

    def __iter__(self):
        return iter(self.stack)

    def add_card(self, card):
        self.stack.append(card)
        self.sort_cards_by_type()

    def remove_card(self, card):
        self.stack.remove(card)

    def get_card_by_index(self, ix):
        return self.stack[ix]

    def print_cards_with_index(self):
        card_index = 0
        msg = []
        for card in self.stack:
            color = "white" if card.value == JOKER or card.value == WIZARD else card.color
            msg.append(click.style("[%d]: %s" % (card_index, str(card)), fg=color))
            card_index += 1
        return ", ".join(msg)

    def sort_cards_by_type(self):
        wizard_jokers = sorted([wj for wj in self.stack if wj.value == JOKER or wj.value == WIZARD],
                               key=lambda x: x.value)
        colored_cards = sorted([cc for cc in self.stack if cc.value != JOKER and cc.value != WIZARD],
                               key=lambda x: (x.color, x.value))
        self.stack = wizard_jokers + colored_cards

    def amount(self):
        return len(self.stack)
