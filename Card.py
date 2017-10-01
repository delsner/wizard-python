WIZARD = 14
JOKER = 0


class Card:
    def __init__(self):
        self.color = ''
        self.value = 0

    def __str__(self):
        return "%d %s" % (self.value, self.color[0])
