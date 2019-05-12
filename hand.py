from models import Deck, Suits, Ranks, Joker, Hands


class Hand:

    def __init__(self, hand):
        self.hand = [[0 for _ in range(len(Suits))] for _ in range(len(Ranks))]
        self.joker = False

        for card in hand:
            if card == Joker:
                self.joker = True
                continue
            rank = Ranks[card[:1]]
            suit = Suits[card[1:]]
            self.hand[rank][suit] += 1

        self.validate()

    def __repr__(self):
        return str(self.cards())

    def validate(self):

        if not 1 == max(map(max, self.hand)):
            raise ValueError("Invalid hand: redundant card(s) in hand")

        if self.joker:
            if not 4 == sum(map(sum, self.hand)):
                raise ValueError("Invalid number of cards in hand: {}".format(sum(map(sum, self.hand))+1))
        else:
            if not 5 == sum(map(sum, self.hand)):
                raise ValueError("Invalid number of cards in hand: {}".format(sum(map(sum, self.hand))))

    def cards(self):
        hand = []
        for i, rank in enumerate(self.hand):
            for j, suit in enumerate(rank):
                if suit:
                    hand.append(Deck[i][j])
        if self.joker:
            hand.append(Joker)
        return hand

    # TODO: Verify: Is Joker always high card?
    def high_card(self):
        return Joker if self.joker else self.cards()[-1:][0]

    def low_card(self):
        return self.cards()[:1][0]

    def identify(self):

        def n_of_a_kind(n):
            def _of_a_kind(hand):
                for rank in hand:
                    if n == sum(rank):
                        return True
                return False
            return _of_a_kind

        is_four_of_a_kind = n_of_a_kind(4)

        is_three_of_a_kind = n_of_a_kind(3)

        is_pair = n_of_a_kind(2)

        def is_five_of_a_kind(hand):
            return self.joker and is_four_of_a_kind(hand)

        def is_flush(hand):
            suits = []
            for rank in hand:
                for i, suit in enumerate(rank):
                    if suit:
                        suits.append(i)
            return min(suits) == max(suits) and (4 == len(suits) if self.joker else 5 == len(suits))

        def is_straight(hand):
            ranks = []
            for i, rank in enumerate(hand):
                if sum(rank):
                    ranks.append(i)
            return (
                3 == max(ranks) - min(ranks) and 4 == len(ranks)  # Joker-assisted straight
                if self.joker else
                4 == max(ranks) - min(ranks) and 5 == len(ranks)  # Natural straight
            )

        # TODO: Verify: Can a joker complete both a flush and a straight at the same time?
        def is_straight_flush(hand):
            if is_flush(hand) and is_straight(hand):
                return True
            return False

        def is_full_house(hand):
            if is_three_of_a_kind(hand) and is_pair(hand):
                return True
            if self.joker and is_two_pair(hand):
                return True
            return False

        def is_two_pair(hand):
            num_pairs = 0
            for rank in hand:
                if 2 == sum(rank):
                    num_pairs += 1
            return 2 == num_pairs

        if is_five_of_a_kind(self.hand):
            return Hands.five_of_a_kind

        if is_straight_flush(self.hand):
            return Hands.straight_flush

        if is_four_of_a_kind(self.hand) or self.joker and is_three_of_a_kind(self.hand):
            return Hands.four_of_a_kind

        if is_full_house(self.hand):
            return Hands.full_house

        if is_flush(self.hand):
            return Hands.flush

        if is_straight(self.hand):
            return Hands.straight

        if is_three_of_a_kind(self.hand) or self.joker and is_pair(self.hand):
            return Hands.three_of_a_kind

        if is_two_pair(self.hand):
            return Hands.two_pair

        if self.joker or is_pair(self.hand):
            return Hands.pair

        return Hands.nothing
