#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 14:09:07 2022

@author: willmcarthur
"""
import random
from poker import Deck, Player, Card
from ranges import build_range, random_hand
from hand_analyzer import determine_hand, winning_hand, valid_hand


def flop(deck):
    flop = [deck.draw_card() for i in range(3)]
    return flop


def turn(deck):
    turn = [deck.draw_card()]
    return turn

def river(deck):
    river = [deck.draw_card()]
    return river


# Tests and code for comparing hands of players including streets

deck = Deck()
players = [Player() for i in range(6)]
all_cards = []
all_hands = []
streets = []

for i in range(2):
    for p in players:
        p.draw(deck)

streets += flop(deck)

streets += turn(deck)

streets += river(deck)  

for p in players:
    all_hands.append(determine_hand(p.hand + streets))
    print(determine_hand(p.hand + streets))
    print("----------------------------")

print("After the river, the winning hand is:")
print(winning_hand(all_hands))

for p in players:
    p.show_hand()
    all_cards += p.hand
    print("----")

if not valid_hand(all_cards):
    print("DANGER DANGER")
    
    