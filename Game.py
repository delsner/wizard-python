from Round import Round

NUMBER_CARDS = 60


class Game:
    def __init__(self):
        self.players = []

    def start(self):
        number_rounds = int(NUMBER_CARDS / len(self.players))
        for nr in range(number_rounds):
            round_ = Round()
            round_.round_number = nr
            round_.players = self.players
            round_.play_round()

    def add_player(self, player):
        self.players.append(player)
