import random


class PlayingCard:

    def __init__(self, suit, value):
        """

        :param suit:
        :param value:
        """
        self._suit = suit
        self._value = value

    def get_value(self):
        return self._value

    def get_suit(self):
        return self._suit


def build_deck():
    """
    Build a full deck of 52 playing cards.

    :return: A list of PlayingCard instances representing a full deck.
    """
    suits = ['Blue', 'Red', 'Yellow', 'Green']
    values = ['Guppy', 'Catfish', 'Bluegill', 'Rainbow Trout', 'Pacific Salmon', 'Betta Fish', 'Octopus', 'Weather Loach',
              'Moray Eel', 'Jack Fish', 'Queen Conch',
              'King Crab', 'Arowana']
    deck = [PlayingCard(suit, value) for suit in suits for value in values]
    random.shuffle(deck)
    return deck


def match_check(hand, match_pile):
    matches = set()
    i = 0
    while i < len(hand):
        card = hand[i]
        if card.get_value() in matches:
            for match_card in hand:
                if match_card.get_value() == card.get_value() and match_card != card:
                    hand.remove(match_card)
                    hand.remove(card)
                    match_pile.append((match_card, card))
        else:
            matches.add(card.get_value())
            i += 1


deck_1 = build_deck()