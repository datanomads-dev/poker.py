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
        print(json.dumps(str(Hand(json.loads(line)))))


if __name__ == '__main__':
    main()
