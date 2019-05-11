A class-based solution to identifying poker hands.

```bash
(py3) rriehle@ontario:~/src/qumulo/poker.py (master)$ cat hand.json
["4D", "2C", "JC", "6H", "8S"]
(py3) rriehle@ontario:~/src/qumulo/poker.py (master)$ python main.py < hand.json
"['2C', '4D', '6H', '8S', 'JC']"
(py3) rriehle@ontario:~/src/qumulo/poker.py (master)$ python -m pytest -vv tests/
===================================================================== test session starts ======================================================================
platform darwin -- Python 3.7.3, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- /Users/brew/.virtualenvs/py3/bin/python
cachedir: .pytest_cache
rootdir: /Users/rriehle/src/qumulo/poker.py
collected 16 items

tests/test_hand.py::test_redundant_cards_raises_error PASSED                                                                                             [  6%]
tests/test_hand.py::test_lite_hand_raises_error PASSED                                                                                                   [ 12%]
tests/test_hand.py::test_heavy_hand_raises_error PASSED                                                                                                  [ 18%]
tests/test_hand.py::test_straight_flush PASSED                                                                                                           [ 25%]
tests/test_hand.py::test_four_of_a_kind PASSED                                                                                                           [ 31%]
tests/test_hand.py::test_full_house PASSED                                                                                                               [ 37%]
tests/test_hand.py::test_flush_of_clubs PASSED                                                                                                           [ 43%]
tests/test_hand.py::test_flush_of_spades PASSED                                                                                                          [ 50%]
tests/test_hand.py::test_straight PASSED                                                                                                                 [ 56%]
tests/test_hand.py::test_three_of_a_kind PASSED                                                                                                          [ 62%]
tests/test_hand.py::test_two_pair PASSED                                                                                                                 [ 68%]
tests/test_hand.py::test_one_pair PASSED                                                                                                                 [ 75%]
tests/test_hand.py::test_nothing PASSED                                                                                                                  [ 81%]
tests/test_hand.py::test_high_card PASSED                                                                                                                [ 87%]
tests/test_hand.py::test_low_card PASSED                                                                                                                 [ 93%]
tests/test_hand.py::test_print_hand PASSED                                                                                                               [100%]

================================================================== 16 passed in 0.04 seconds ===================================================================
(py3) rriehle@ontario:~/src/qumulo/poker.py (master)$
```

