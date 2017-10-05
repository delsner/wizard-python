import Dealer
import Players
import Console_Output

NUMBER_CARDS = 60


class Game:
    def __init__(self):
        self.players = Players.Players()

    def start(self):
        number_rounds = int(NUMBER_CARDS / self.players.num_players())
        dealer = Dealer.Dealer()
        for round_number in range(1, number_rounds + 1):
            dealer.reset_card_deck()
            dealer.deal_cards(players=self.players, amount=round_number)
            trump_color = dealer.determine_trump()
            Console_Output.print_new_round_info(round_number, trump_color)
            self.players.play_round(round_number, trump_color)
        self.determine_winners()

    def add_player(self, player):
        self.players.add_player(player)

    def determine_winners(self):
        winners_value = sorted(self.players, key=lambda x: x.value)[-1]
        for p in filter(lambda x: x.value == winners_value, self.players):
            Console_Output.print_winner(p.name)
