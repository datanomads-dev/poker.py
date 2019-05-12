A class-based solution to identifying poker hands.

# Usage


```bash
(py3) rriehle@ontario:~/src/qumulo/poker.py (joker)$ cat hand.json
["5C", "6D", "7H", "8S", "9C"]
["4D", "2C", "JC", "6H", "8S"]
(py3) rriehle@ontario:~/src/qumulo/poker.py (joker)$ python main.py < hand.json
"['5C', '6D', '7H', '8S', '9C']"
Hands.straight
Low card: 5C
High card: 9C
"['2C', '4D', '6H', '8S', 'JC']"
Hands.nothing
Low card: 2C
High card: JC
```

# Test coverage

Test names are a hint toward the capabilities of the system.

```bash
(py3) rriehle@ontario:~/src/qumulo/poker.py (joker)$ python -m pytest -vv tests/
===================================================================== test session starts ======================================================================
platform darwin -- Python 3.7.3, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- /Users/brew/.virtualenvs/py3/bin/python
cachedir: .pytest_cache
rootdir: /Users/rriehle/src/qumulo/poker.py
collected 25 items

tests/test_hand.py::test_redundant_cards_raises_error PASSED                                                                                             [  4%]
tests/test_hand.py::test_lite_hand_raises_error PASSED                                                                                                   [  8%]
tests/test_hand.py::test_heavy_hand_raises_error PASSED                                                                                                  [ 12%]
tests/test_hand.py::test_five_of_a_kind PASSED                                                                                                           [ 16%]
tests/test_hand.py::test_straight_flush PASSED                                                                                                           [ 20%]
tests/test_hand.py::test_four_of_a_kind PASSED                                                                                                           [ 24%]
tests/test_hand.py::test_four_of_a_kind_joker_assisted PASSED                                                                                            [ 28%]
tests/test_hand.py::test_full_house PASSED                                                                                                               [ 32%]
tests/test_hand.py::test_full_house_joker_assisted_two_pair PASSED                                                                                       [ 36%]
tests/test_hand.py::test_flush_of_clubs PASSED                                                                                                           [ 40%]
tests/test_hand.py::test_flush_of_clubs_joker_assisted PASSED                                                                                            [ 44%]
tests/test_hand.py::test_flush_of_spades PASSED                                                                                                          [ 48%]
tests/test_hand.py::test_flush_of_spades_joker_assisted PASSED                                                                                           [ 52%]
tests/test_hand.py::test_straight PASSED                                                                                                                 [ 56%]
tests/test_hand.py::test_straight_joker_assisted PASSED                                                                                                  [ 60%]
tests/test_hand.py::test_three_of_a_kind PASSED                                                                                                          [ 64%]
tests/test_hand.py::test_three_of_a_kind_joker_assisted PASSED                                                                                           [ 68%]
tests/test_hand.py::test_two_pair PASSED                                                                                                                 [ 72%]
tests/test_hand.py::test_one_pair PASSED                                                                                                                 [ 76%]
tests/test_hand.py::test_joker_assisted_pair PASSED                                                                                                      [ 80%]
tests/test_hand.py::test_nothing PASSED                                                                                                                  [ 84%]
tests/test_hand.py::test_high_card PASSED                                                                                                                [ 88%]
tests/test_hand.py::test_high_card_with_joker PASSED                                                                                                     [ 92%]
tests/test_hand.py::test_low_card PASSED                                                                                                                 [ 96%]
tests/test_hand.py::test_print_hand PASSED                                                                                                               [100%]

================================================================== 25 passed in 0.05 seconds ===================================================================
(py3) rriehle@ontario:~/src/qumulo/poker.py (joker)$
```

# Data Model

Among the most important decisions in the development of tractable, extendable solutions are those around the data model. In other words, this question is key: How should the entities in the domain be represented as data? For the present case I have chosen a matrix with suits (Clubs, Hearts, etc.) across one dimension and ranks (Ace, King, Queen, etc.) along the other. In Python the matrix could take the form of nested tuples or lists, or a Numpy array.

```python
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
```

A straight, which upon being presented as input to the program might look like this:

```json
["5C", "6D", "7H", "8S", "9C"]
```

This is the straight above ingested into its internal representation:

```python
straight = [
#  C  D  H  Spades
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 0, 0, 0],  # 5
  [0, 1, 0, 0],  # 6
  [0, 0, 1, 0],  # 7
  [0, 0, 0, 1],  # 8
  [1, 0, 0, 0],  # 9
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
]
```

# Hand Identification

Once ingested a hand is treated as an immutable object. Functions (or methods) are run across the matrix to make observations about the hand. Three of a kind, for instance, would be detected by the following function.

```python
def three_of_a_kind(hand):
    for rank in hand:
        if 3 == sum(rank):
            return True
    return False
```

Identification of ranking hands is done in order, so for instance full house is tested before three of a kind thereby preventing mis-identification.

# Joker

Joker does not fit into the fifty-two card matrix of the data model. Introduction of a joker boolean to the hand object was a straightforward task and added little complexity to the identification algorithm. This was an easy feature addition which added confidence in the data model.

# TODO

Account for declared wild cards such as "Fours are wild" or "One-eyed Jacks are wild."  One strategy would be to populate the hand matrix with the wild cards along with the rest of the cards. The identification algorithm would require little or no modification. The ingest and extraction methods (```__init__``` and ```__repr__``` respectively) would need consideration.
