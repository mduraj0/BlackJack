from player import Player
from card import Card


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
