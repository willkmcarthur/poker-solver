# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 10:32:00 2021

@author: willmcarthur

This file contains all of the range information for the poker project
"""

import random
from poker import Deck
from settings import ranks, ranges

deck = Deck()

# Create a list of all pocket pairs for a given rank
def pocket_pairs(rank):
    all_rank = [r for r in deck.cards if r.rank == rank]
    pairs = []
    i = -1
    while i < len(all_rank):
        i += 1
        j = i+1
        while j < len(all_rank):
            pairs.append((all_rank[i], all_rank[j]))
            j += 1
    return pairs

# Create a list of all pocket pairs for a range between two ranks
def range_of_pairs(high, low):
    i = ranks.index(low)
    many_pairs = []
    while i <= ranks.index(high):
        many_pairs.append(pocket_pairs(ranks[i]))
        i += 1
    return many_pairs

# Create a list of all off-suited hand variations for two ranks
def off_suited(high, low):
    all_high = [h for h in deck.cards if h.rank == high]
    all_low = [l for l in deck.cards if l.rank == low]
    off_suited = []
    for h in all_high:
        for l in all_low:
            if l.suit != h.suit:
                off_suited.append((h, l))
    return off_suited

# Create a list of all off-suited hand possibilities between two ranks
def range_of_off_suited(high, low):
    i = ranks.index(low)
    j = ranks.index(high)
    many_off = []
    while i < j:
        many_off.append(off_suited(ranks[i],ranks[j]))
        i += 1
    return many_off

# Create a list of all suited hand variations for two ranks
def suited(high, low):
    all_high = [h for h in deck.cards if h.rank == high]
    all_low = [l for l in deck.cards if l.rank == low]
    suited = []
    for h in all_high:
        for l in all_low:
            if l.suit == h.suit:
                suited.append((h, l))
                break
    return suited

# Create a list of all suited hand possibilities between two ranks
def range_of_suited(high, low):
    i = ranks.index(low)
    j = ranks.index(high)
    many_suited = []
    while i < j:
        many_suited.append(suited(ranks[i],ranks[j]))
        i += 1
    return many_suited

# Create a list of all hands for a given position
def build_range(position):
    card_range = []
    hands = []
    # Using our suited, off-suited, and pairs functions, we can build a range
    # based on the position of the player
    for r in ranges[position]["suited"]:
        card_range += range_of_suited(r[0], r[1])
    for r in ranges[position]["off-suited"]:
        card_range += range_of_off_suited(r[0], r[1])
    for r in ranges[position]["pairs"]:
        card_range += range_of_pairs(r[0], r[1])
    
    if position == "UTG":
        card_range += [suited("A","5")]
    elif position == "UTG2":
        card_range += [suited("A","5")]
        card_range += [suited("A","4")]
    
    for u in card_range:
        for p in u:
            hands.append(p)
            
    return hands

# Return a random hand from a list of hands
def random_hand(hands):
    randint = random.randint(0, len(hands)-1)
    return hands[randint]


for r in ranges:
    print("----")
    print("A random hand in the " + r + " range:")
    for s in random_hand(build_range(r)):
        s.show()
        