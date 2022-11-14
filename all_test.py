import pytest
from card import Card, InvalidColor, InvalidValue
from deck import Deck
from player import Player


def test_give_calculate_points():
    card_1 = Card('Hearts', 2)
    card_2 = Card('Clubs', 5)
    player = Player()
    player.take_card(card_1)
    player.take_card(card_2)

    assert player.calculate_points() == 7


def test_calculate_points_with_two_aces():
    card_1 = Card('Hearts', 'ACE')
    card_2 = Card('Clubs', 'ACE')
    player = Player()
    player.take_card(card_1)
    player.take_card(card_2)
    assert player.calculate_points() == 21


def test_calculate_points_with_ace_and_two_cards():
    card_1 = Card('Hearts', 'ACE')
    card_2 = Card('Clubs', 5)
    player = Player()
    player.take_card(card_1)
    player.take_card(card_2)
    assert player.calculate_points() == 16


def test_calculate_points_with_3_aces():
    card_1 = Card('Hearts', 'ACE')
    card_2 = Card('Clubs', 'ACE')
    card_3 = Card('Diamond', 'ACE')
    player = Player()
    player.take_card(card_1)
    player.take_card(card_2)
    player.take_card(card_3)
    assert player.calculate_points() == 3


# -------------------------------------------------------------------------- card test-------------------------------


def test_creation():
    """Test card creation"""
    card = Card('Hearts', 'ACE')
    print(card.value)
    assert card.color == '♥'
    assert card.value == 'ACE'


def test_invalid_value():
    """Test if is wrong value"""
    with pytest.raises(InvalidValue) as e:
        card = Card('Hearts', 'KING]')
        assert e == 'Invalid card value'


def test_invalid_color():
    """Test if is wrong color"""
    with pytest.raises(InvalidColor) as e:
        card = Card('xxx', 'ACE')
        assert e == 'Invalid card color'


def test_repr():
    """Test if is wrong repr"""
    assert repr(Card('Spades', 'KING')) == 'KING - ♤'
    assert repr(Card('Hearts', 'ACE')) == 'ACE - ♥'
    assert repr(Card('Clubs', 'KING')) == 'KING - ♧'
    assert repr(Card('Diamond', 'KING')) == 'KING - ♦'

#------------------------------- DECK TEST -----------------------------------------


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
