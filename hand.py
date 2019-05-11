from models import Suits, Ranks, Hands


class Hand:

    def __init__(self, hand):
        self.hand = [[0 for _ in range(len(Suits))] for _ in range(len(Ranks))]

        for card in hand:
            rank = Ranks[card[:1]]
            suit = Suits[card[1:]]
            self.hand[rank][suit] += 1

        self.validate()

    def validate(self):

        if not 1 == max(map(max, self.hand)):
            raise ValueError("Invalid hand: redundant card(s)")

        if not 5 == sum(map(sum, self.hand)):
            raise ValueError("Invalid number of cards in hand {}".format(sum(map(sum, self.hand))))

    def identify(self):

        def is_four_of_a_kind(hand):
            for rank in hand:
                if 4 == sum(rank):
                    return True
            return False

        def is_three_of_a_kind(hand):
            for rank in hand:
                if 3 == sum(rank):
                    return True
            return False

        def is_pair(hand):
            for rank in hand:
                if 2 == sum(rank):
                    return True
            return False

        def is_flush(hand):
            suits = []
            for rank in self.hand:
                for i, suit in enumerate(rank):
                    if suit:
                        suits.append(i)
            return min(suits) == max(suits) and 5 == len(suits)

        def is_straight(hand):
            ranks = []
            for i, rank in enumerate(hand):
                if sum(rank):
                    ranks.append(i)
            return 4 == max(ranks) - min(ranks) and 5 == len(ranks)

        def is_straight_flush(hand):
            if is_flush(hand) and is_straight(hand):
                return True
            return False

        def is_full_house(hand):
            if is_three_of_a_kind(hand) and is_pair(hand):
                return True
            return False

        def is_two_pair(hand):
            num_pairs = 0
            for rank in hand:
                if 2 == sum(rank):
                    num_pairs += 1
            return 2 == num_pairs

        if is_straight_flush(self.hand):
            return Hands.straight_flush

        if is_four_of_a_kind(self.hand):
            return Hands.four_of_a_kind

        if is_full_house(self.hand):
            return Hands.full_house

        if is_flush(self.hand):
            return Hands.flush

        if is_straight(self.hand):
            return Hands.straight

        if is_three_of_a_kind(self.hand):
            return Hands.three_of_a_kind

        if is_two_pair(self.hand):
            return Hands.two_pair

        if is_pair(self.hand):
            return Hands.pair

        return Hands.nothing
