from Card import WIZARD, JOKER


class Trick:
    def __init__(self):
        self.cards = []
        self.trump_color = ""
        self.base_card = None

    def receive_card(self, card):
        self.cards.append(card)
        self.set_base_card(card)

    def set_base_card(self, card):
        if self.base_card is None or self.base_card.value == JOKER:
            self.base_card = card

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
            elif c.color == self.trump_color and winner_card != self.trump_color:
                winner_card = c
        return self.cards.index(winner_card)

    def validate_requested_card(self, card, hand_cards):
        '''
        Validates the card that a player desires to play based on this trick's cards and the hand cards of the player.
        :param card: 
        :param hand_cards: 
        :return: True if valid card 
        '''
        if self.base_card is None or self.base_card.value == WIZARD or self.base_card.value == JOKER:
            return True

        filtered_hand_cards = filter(lambda x: x.color == self.base_card.color, hand_cards)
        if len(list(filtered_hand_cards)) > 0 and card.color != self.base_card.color:
            return False
        return True
