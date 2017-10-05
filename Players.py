import Console_Output
import Trick
import click


class Players:
    def __init__(self):
        self._players = []
        self._start_player_next_round = None

    def add_player(self, player):
        self._players.append(player)

    def num_players(self):
        return len(self._players)

    def __iter__(self):
        return iter(self._players)

    def play_round(self, round_nr, trump_color):
        self._start_player_next_round = self._players[1]
        self.reset_trick_guesses()
        self.request_trick_guesses()
        self.play_tricks(round_nr, trump_color)
        self.update_scores()
        Console_Output.print_current_scores(self._players)
        self.rotate_players_to_player(self._start_player_next_round)

    def request_trick_guesses(self):
        for p in self._players:
            p.guess_tricks()

    def reset_trick_guesses(self):
        for p in self._players:
            p.reset_tricks()

    def play_tricks(self, nr_hand_cards=0, trump_color=""):
        for _ in range(nr_hand_cards):
            self.play_one_trick(trump_color)

    def play_one_trick(self, trump_color):
        t = Trick.Trick(trump_color=trump_color)
        for p in self._players:
            p.play_card(t)
        winner_card_ix = t.determine_winner()
        winner = self._players[winner_card_ix]
        winner.won_tricks += 1
        Console_Output.print_trick_winner(winner.name)
        # set winning player as first to act for the next trick
        self.rotate_players_to_player(winner)

    def rotate_players_to_player(self, player):
        ix = self._players.index(player)
        self._players = self._players[ix:] + self._players[:ix]

    def update_scores(self):
        for p in self._players:
            p.score += p.won_tricks
            if p.guessed_tricks == p.won_tricks:
                p.score += 5
