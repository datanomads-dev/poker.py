from enum import Enum


Deck = (
    # Clubs, Diamonds, Hearts, Spades
    ('2C', '2D', '2H', '2S'),
    ('3C', '3D', '3H', '3S'),
    ('4C', '4D', '4H', '4S'),
    ('5C', '5D', '5H', '5S'),
    ('6C', '6D', '6H', '6S'),
    ('7C', '7D', '7H', '7S'),
    ('8C', '8D', '8H', '8S'),
    ('9C', '9D', '9H', '9S'),  # Nines
    ('TC', 'TD', 'TH', 'TS'),  # Tens
    ('JC', 'JD', 'JH', 'JS'),  # Jacks
    ('QC', 'QD', 'QH', 'QS'),  # Queens
    ('KC', 'KD', 'KH', 'KS'),  # Kings
    ('AC', 'AD', 'AH', 'AS'),  # Aces
)


Suits = {
    'S': 3,  # Spades
    'H': 2,  # Hearts
    'D': 1,  # Diamonds
    'C': 0,  # Clubs
}


Ranks = {
    'A': 12,  # Ace
    'K': 11,  # King
    'Q': 10,  # Queen
    'J': 9,  # Jack
    'T': 8,  # Ten
    '9': 7,  # Nine
    '8': 6,
    '7': 5,
    '6': 4,
    '5': 3,
    '4': 2,
    '3': 1,
    '2': 0,
}


class Hands(Enum):
    straight_flush = 8
    four_of_a_kind = 7
    full_house = 6
    flush = 5
    straight = 4
    three_of_a_kind = 3
    two_pair = 2
    pair = 1
    nothing = 0
