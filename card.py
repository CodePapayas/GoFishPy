import random
from collections import Counter

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
    from collections import Counter

    # Count occurrences of each card value
    card_count = Counter(card.get_value() for card in hand)

    # Find cards that appear exactly four times
    cards_to_remove = [value for value, count in card_count.items() if count == 4]

    for card_value in cards_to_remove:
        cards_removed = []
        for card in hand[:]:
            if card.get_value() == card_value:
                hand.remove(card)
                cards_removed.append(card)
                if len(cards_removed) == 4:
                    match_pile.append(tuple(cards_removed))
                    break
        if len(cards_removed) < 4:
            hand_name = "AI Hand" if "ai" in match_pile.__repr__() else "Player Hand"
            print(
                f"Debug: Failed to remove 4 cards from {hand_name} for value {card_value}. Only removed {len(cards_removed)}.")
