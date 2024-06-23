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


deck_1 = build_deck()