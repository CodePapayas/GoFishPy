# Author: Zachary Wilkins-Olson

from card import *
from termcolor import colored, cprint
from prettytable import PrettyTable
from ai_logic import *


class CardGame:
    def __init__(self):
        self._deck = build_deck()
        self._player_deck = []
        self._player_match_pile = []
        self._player_table = PrettyTable()
        self._ai_deck = []
        self._ai_match_pile = []
        self._ai_table = PrettyTable()

        self._player_table.field_names = [colored("Player Hand", 'white', 'on_magenta', attrs=["bold"])]
        self._ai_table.field_names = [colored("AI Hand", 'black', 'on_cyan', attrs=["bold"])]

    def deal_cards(self):
        dealer_tracker = 0
        cards_dealt = 0

        while cards_dealt < 14:
            dealt_card = self._deck.pop(0)
            if dealer_tracker % 2 == 0:
                self._player_deck.append(dealt_card)
            else:
                self._ai_deck.append(dealt_card)
            dealer_tracker += 1
            cards_dealt += 1

    def populate_tables(self):
        self._player_table.clear_rows()
        self._ai_table.clear_rows()

        for card in self._player_deck:
            if card.get_suit() == 'Red':
                self._player_table.add_row([colored(card.get_value(), "red")])
            elif card.get_suit() == 'Blue':
                self._player_table.add_row([colored(card.get_value(), "blue")])
            elif card.get_suit() == 'Yellow':
                self._player_table.add_row([colored(card.get_value(), "yellow")])
            elif card.get_suit() == 'Green':
                self._player_table.add_row([colored(card.get_value(), "green")])

        for card in self._ai_deck:
            if card.get_suit() == 'Red':
                self._ai_table.add_row([colored(card.get_value(), "red")])
            elif card.get_suit() == 'Blue':
                self._ai_table.add_row([colored(card.get_value(), "blue")])
            elif card.get_suit() == 'Yellow':
                self._ai_table.add_row([colored(card.get_value(), "yellow")])
            elif card.get_suit() == 'Green':
                self._ai_table.add_row([colored(card.get_value(), "green")])

    def ai_turn(self):
        match_check(self._ai_deck, self._ai_match_pile)
        self.populate_tables()
        hand = self._ai_deck

    def player_turn(self):
        match_check(self._player_deck, self._player_match_pile)
        self.populate_tables()

    def print_tables(self):
        print("AI Hand:")
        print(self._ai_table)
        print("\nPlayer Hand:")
        print(self._player_table)


# Instantiate the game and run it
game = CardGame()
game.deal_cards()
game.populate_tables()
game.print_tables()
game.player_turn()
game.ai_turn()
game.print_tables()
