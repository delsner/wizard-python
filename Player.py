import click

from Card import JOKER, WIZARD


class Player:
    def __init__(self):
        self.name = ""
        self.cards = set()
        self.guess = 0
        self.tricks = 0

    def deal_card(self, card):
        self.cards.add(card)

    def request_card(self):
        wizard_jokers = sorted(filter(lambda x: x.value == JOKER or x.value == WIZARD, self.cards),
                               key=lambda x: x.value)
        colored_cards = self.cards - set(wizard_jokers)
        colored_cards = sorted(colored_cards, key=lambda x: (x.color, x.value))
        card_index = 0
        for card in wizard_jokers:
            card_index += 1
            click.echo(click.style(str(card), fg="white"))
        for card in colored_cards:
            card_index += 1
            click.echo(click.style(str(card), fg=card.color))
        selected_index = click.prompt("Choose index: ", type=int)

        all_cards = wizard_jokers + colored_cards
        return all_cards[selected_index]
