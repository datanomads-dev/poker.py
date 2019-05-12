#!/usr/bin/env python3

import json
from sys import stdin

from hand import Hand


def main():
    """
    Take a series of cards as json from stdin,
    load them into a hand and print them out,
    merely to demonstrate that the class/program works.

    usage:

    $ python main.py < hand.json
    """

    for line in stdin:
        hand = Hand(json.loads(line))
        print(json.dumps(str(hand)))
        print(hand.identify())
        print("Low card: {}".format(hand.low_card()))
        print("High card: {}".format(hand.high_card()))


if __name__ == '__main__':
    main()
