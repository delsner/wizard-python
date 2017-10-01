from Stack import Stack
from Trick import Trick


class Round:
    def __init__(self):
        self.stack = Stack()
        self.round_number = 0
        self.players = []

    def deal_cards(self):
        for _ in range(self.round_number):
            for player in self.players:
                player.deal_card(self.stack.draw_card())

    def request_tricks(self):
        pass

    def play_trick(self):
        # returns winner of trick
        t = Trick()
        for p in self.players:
            t.receive_card(p.request_card())
        return t.determine_winner()

    def play_round(self):
        self.deal_cards()
        self.request_tricks()
        for _ in range(self.round_number):
            ind = self.play_trick()
            self.players = self.players[ind:] + self.players[:ind]
        self.evaluate_score()

    def evaluate_score(self):
        pass
