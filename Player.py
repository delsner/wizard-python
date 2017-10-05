import Cards
import Console_Output


class Player:
    def __init__(self):
        self.name = ""
        self.cards = Cards.Cards()
        self.guessed_tricks = 0
        self.won_tricks = 0
        self.score = 0

    def receive_card(self, card):
        self.cards.add_card(card)

    def play_card(self, trick):
        requested_card = self.select_card()
        while not trick.validate_requested_card(requested_card, self.cards):
            requested_card = self.select_card()
        self.cards.remove_card(requested_card)
        trick.receive_card(requested_card)

    def select_card(self):
        Console_Output.print_hand_card_information(self.name, self.cards)
        selected_index = -1
        while selected_index < 0 or selected_index >= self.cards.amount():
            selected_index = Console_Output.choose_card_dialog(self.name)
        return self.cards.get_card_by_index(selected_index)

    def guess_tricks(self):
        Console_Output.print_hand_card_information(self.name, self.cards)
        requested_tricks = -1
        while not (requested_tricks <= self.cards.amount() and requested_tricks >= 0):
            requested_tricks = Console_Output.guess_tricks_dialog(self.name)
        self.guessed_tricks = requested_tricks

    def reset_tricks(self):
        self.won_tricks = 0
