import random
from card import Card


class Deck:

    def __init__(self):
        self.cards = []
        for color in Card.possible_colors:
            for value in Card.possible_values:
                self.cards.append(Card(color=color, value=value))

    def shuffle(self):
        random.shuffle(self.cards)

    def hit_card(self):
        return self.cards.pop()

