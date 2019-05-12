A class-based solution to identifying poker hands.

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

