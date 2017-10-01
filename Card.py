WIZARD = 15
JOKER = 0


class Card:
    def __init__(self):
        self.color = None
        self.card_value = None

    def __str__(self):
        return "%d%s" % (self.card_value, self.color[0])