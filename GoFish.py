from card import *
from termcolor import colored, cprint
from prettytable import PrettyTable

deck = build_deck()
player_deck = []
player_match_pile = []
player_table = PrettyTable()
ai_deck = []
ai_match_pile = []
ai_table = PrettyTable()

# Set up table headers
player_table.field_names = ["Player Hand"]
ai_table.field_names = ["AI Hand"]

# Deal cards to player and AI
dealer_tracker = 1
cards_dealt = 0

while cards_dealt < 14:
    dealt_card = deck.pop(0)
    if dealer_tracker % 2 == 0:
        player_deck.append(dealt_card)
    else:
        ai_deck.append(dealt_card)
    dealer_tracker += 1
    cards_dealt += 1

# Add player cards to the table with colors
for card in player_deck:
    if card.get_suit() == 'Red':
        player_table.add_row([colored(card.get_value(), "red")])
    elif card.get_suit() == 'Blue':
        player_table.add_row([colored(card.get_value(), "blue")])
    elif card.get_suit() == 'Yellow':
        player_table.add_row([colored(card.get_value(), "yellow")])
    elif card.get_suit() == 'Green':
        player_table.add_row([colored(card.get_value(), "green")])

# Add AI cards to the table with colors
for card in ai_deck:
    if card.get_suit() == 'Red':
        ai_table.add_row([colored(card.get_value(), "red")])
    elif card.get_suit() == 'Blue':
        ai_table.add_row([colored(card.get_value(), "blue")])
    elif card.get_suit() == 'Yellow':
        ai_table.add_row([colored(card.get_value(), "yellow")])
    elif card.get_suit() == 'Green':
        ai_table.add_row([colored(card.get_value(), "green")])

# Print the tables
print("AI Hand:")
print(ai_table)
print("\nPlayer Hand:")
print(player_table)
