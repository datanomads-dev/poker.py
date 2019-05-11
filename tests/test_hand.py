#!/usr/bin/env python3

import pytest

from models import Hands
from hand import Hand


def test_redundant_cards_raises_error():
    with pytest.raises(ValueError):
        Hand(['5H', '6S', '5H', '5H', '6S'])

def test_lite_hand_raises_error():
    with pytest.raises(ValueError):
        Hand(['5H', '6H', '7H', '9H'])

def test_heavy_hand_raises_error():
    with pytest.raises(ValueError):
        Hand(['5H', '6S', '3H', '5C', '2D', '3S'])

def test_straight_flush():
    assert Hands.straight_flush == Hand(['TC', '7C', '9C', 'JC', '8C']).identify()


def test_four_of_a_kind():
    assert Hands.four_of_a_kind == Hand(['6D', '6C', '6H', '2D', '6S']).identify()


def test_full_house():
    assert Hands.full_house == Hand(['5H', '5C', '5S', '6S', '6C']).identify()


def test_flush_of_clubs():
    assert Hands.flush == Hand(['3C', 'TC', '9C', '7C', 'QC']).identify()


def test_flush_of_spades():
    assert Hands.flush == Hand(['2S', 'TS', '9S', 'AS', 'QS']).identify()


def test_straight():
    assert Hands.straight == Hand(['5C', '6D', '7H', '8S', '9C']).identify()


def test_three_of_a_kind():
    assert Hands.three_of_a_kind == Hand(['TD', 'TH', 'TC', '4C', '3H']).identify()


def test_two_pair():
    assert Hands.two_pair == Hand(['AD', 'AH', '6C', '6S', '3D']).identify()


def test_one_pair():
    assert Hands.pair == Hand(['KD', 'JC', 'KS', '6D', '2S']).identify()
