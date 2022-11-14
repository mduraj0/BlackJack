"""Black Jack Python Game"""


class InvalidValue(Exception):
    """My exception for test, checking value"""


class InvalidColor(Exception):
    """My exception for test, checking correct color"""


class Card:
    """Creating card"""

    possible_colors = {
        'Diamond': '♦',
        'Hearts': '♥',
        'Clubs': '♧',
        'Spades': '♤'
    }

    possible_values = list(range(2, 11)) + ['ACE', 'JACK', 'KING', 'QUEEN']

    def __init__(self, color, value):
        if color not in self.possible_colors:
            raise InvalidColor('Invalid card color')

        self.color = self.possible_colors[color]

        if value not in self.possible_values:
            raise InvalidValue('Invalid card value!!')

        self.value = value

    def __repr__(self):
        return f'{self.value} - {self.color}'


