#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 14:09:07 2022

@author: willmcarthur

This file is meant to test the streets of a poke game including the flop, turn, and river
It might need to be removed entirely or refactored into a different file
"""
import random
from poker import Deck, Player, Card
from ranges import build_range, random_hand
from hand_analyzer import determine_hand, winning_hand, valid_hand

# Return the top 3 cards of the deck in the flop
def flop(deck):
    flop = [deck.draw_card() for i in range(3)]
    return flop

# Return the top card of the deck in the turn
def turn(deck):
    turn = [deck.draw_card()]
    return turn

# Return the top card of the deck in the river
def river(deck):
    river = [deck.draw_card()]
    return river


# Tests and code for comparing hands of players including streets

# Initialize deck, players, and streets
deck = Deck()
players = [Player() for i in range(6)]
all_cards = []
all_hands = []
streets = []

# Draw two cards for each player
for i in range(2):
    for p in players:
        p.draw(deck)

# Draw the streets
streets += flop(deck)
streets += turn(deck)
streets += river(deck)  

# Determine the hands of each player by combining the player's hand with the community cards
for p in players:
    all_hands.append(determine_hand(p.hand + streets))
    print(determine_hand(p.hand + streets))
    print("----------------------------")

# Determine the winning hand
print("After the river, the winning hand is:")
print(winning_hand(all_hands))

# Show all the hands
for p in players:
    p.show_hand()
    all_cards += p.hand
    print("----")

# If something went wrong, print a warning
if not valid_hand(all_cards):
    print("DANGER DANGER")