from deck import Deck
from card import Card


def test_creation():
    deck = Deck()
    assert len(deck.cards) == 52


def test_deck():
    deck = Deck()
    cards = [(card.value, card.color) for card in deck.cards]
    for color in Card.possible_colors.values():
        cards_in_color = [card for card in cards if card[1] == color]
        assert len(cards_in_color) == 13


def test_shuffle():
    deck = Deck()
    cards = deck.cards.copy()
    deck.shuffle()
    assert cards != deck.cards


def test_hitted_card():
    deck = Deck()
    last_card = deck.cards[-1]
    hit_card = deck.hit_card()
    assert last_card == hit_card


def test_deck_after_hit():
    deck = Deck()
    card = deck.hit_card()
    deck_hit = deck.cards
    assert len(deck.cards) == 51
    assert card not in deck.cards



