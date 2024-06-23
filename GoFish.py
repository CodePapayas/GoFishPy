from card import *
from termcolor import colored, cprint
from prettytable import PrettyTable

class CardGame:
    def __init__(self):
        self.deck = build_deck()
        self.player_deck = []
        self.player_match_pile = []
        self.player_table = PrettyTable()
        self.ai_deck = []
        self.ai_match_pile = []
        self.ai_table = PrettyTable()

        # Set up table headers
        self.player_table.field_names = ["Player Hand"]
        self.ai_table.field_names = ["AI Hand"]

    def deal_cards(self):
        dealer_tracker = 0
        cards_dealt = 0

        while cards_dealt < 14:
            dealt_card = self.deck.pop(0)
            if dealer_tracker % 2 == 0:
                self.player_deck.append(dealt_card)
            else:
                self.ai_deck.append(dealt_card)
            dealer_tracker += 1
            cards_dealt += 1

    def populate_tables(self):
        for card in self.player_deck:
            if card.get_suit() == 'Red':
                self.player_table.add_row([colored(card.get_value(), "red")])
            elif card.get_suit() == 'Blue':
                self.player_table.add_row([colored(card.get_value(), "blue")])
            elif card.get_suit() == 'Yellow':
                self.player_table.add_row([colored(card.get_value(), "yellow")])
            elif card.get_suit() == 'Green':
                self.player_table.add_row([colored(card.get_value(), "green")])

        for card in self.ai_deck:
            if card.get_suit() == 'Red':
                self.ai_table.add_row([colored(card.get_value(), "red")])
            elif card.get_suit() == 'Blue':
                self.ai_table.add_row([colored(card.get_value(), "blue")])
            elif card.get_suit() == 'Yellow':
                self.ai_table.add_row([colored(card.get_value(), "yellow")])
            elif card.get_suit() == 'Green':
                self.ai_table.add_row([colored(card.get_value(), "green")])

    def print_tables(self):
        print("AI Hand:")
        print(self.ai_table)
        print("\nPlayer Hand:")
        print(self.player_table)

# Instantiate the game and run it
game = CardGame()
game.deal_cards()
game.populate_tables()
game.print_tables()
