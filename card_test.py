"""TEST FILE"""

import pytest
from card import Card, InvalidColor, InvalidValue


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
