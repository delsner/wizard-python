import click
from Card import JOKER, WIZARD


class Player:
    def __init__(self):
        self.name = ""
        self.cards = set()
        self.guess = 0
        self.guessed_tricks = 0
        self.won_tricks = 0
        self.score = 0

    def deal_card(self, card):
        self.cards.add(card)

    def play_card(self, card):
        self.cards.remove(card)
        return card

    def request_card(self):
        self.print_cards()
        all_cards = self.sort_cards_by_type()
        selected_index = -1
        while selected_index < 0 or selected_index >= len(all_cards):
            selected_index = click.prompt("%s, choose card index" % self.name, type=int)
        return all_cards[selected_index]

    def request_tricks(self):
        self.print_cards()
        return click.prompt('%s, how many tricks will you make?' % self.name, type=int)

    def reset_tricks(self):
        self.guessed_tricks = 0
        self.won_tricks = 0

    def print_cards(self):
        click.echo('%s, these are your current cards:' % self.name)
        wizard_jokers, colored_cards = self.sort_cards_by_type(concatenated=False)
        card_index = 0
        for card in wizard_jokers:
            click.echo(click.style("[%d]: %s" % (card_index, str(card)), fg="white"))
            card_index += 1
        for card in colored_cards:
            click.echo(click.style("[%d]: %s" % (card_index, str(card)), fg=card.color))
            card_index += 1

    def sort_cards_by_type(self, concatenated=True):
        wizard_jokers = sorted(filter(lambda x: x.value == JOKER or x.value == WIZARD, self.cards),
                               key=lambda x: x.value)
        colored_cards = self.cards - set(wizard_jokers)
        colored_cards = sorted(colored_cards, key=lambda x: (x.color, x.value))
        if concatenated is False:
            return wizard_jokers, colored_cards
        return wizard_jokers + colored_cards

    def __str__(self) -> str:
        return self.name
