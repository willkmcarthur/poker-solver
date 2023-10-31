#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 10:32:00 2021

@author: willmcarthur
"""

import random
from poker import Deck

deck = Deck()
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
ranges = {
    "UTG" : {
        "suited" : [("A", "T"), ("K","T"), ("Q", "T"), ("J", "9"), ("T", "9"), ("9","8")],
        "off-suited" : [("A", "Q")],
        "pairs" : [("A", "7")]
        },
    "UTG2" : {
        "suited" : [("A", "8"), ("K","9"), ("Q", "9"), ("J", "9"), ("T", "9"), ("9","8")],
        "off-suited" : [("A", "J")],
        "pairs" : [("A", "7")]
        },
    "LJ" : {
        "suited" : [("A", "2"), ("K","9"), ("Q", "9"), ("J", "9"), ("T", "8"), ("9","8"), ("8", "7"), ("7", "6")],
        "off-suited" : [("A", "J"), ("K", "Q")],
        "pairs" : [("A", "5")]
        },
    "HJ" : {
        "suited" : [("A", "2"), ("K","9"), ("Q", "9"), ("J", "9"), ("T", "8"), ("9","7"), ("8", "7"), ("7", "6"), ("6", "5")],
        "off-suited" : [("A", "T"), ("K", "J"), ("Q", "J")],
        "pairs" : [("A", "4")]
        },
    "CO" : {
        "suited" : [("A", "2"), ("K","8"), ("Q", "8"), ("J", "8"), ("T", "8"), ("9","7"), ("8", "6"), ("7", "6"), ("6", "5"), ("5", "4")],
        "off-suited" : [("A", "T"), ("K", "T"), ("Q", "T"), ("J", "T")],
        "pairs" : [("A", "2")]
        },
    "BTN" : {
        "suited" : [("A", "2"), ("K","3"), ("Q", "5"), ("J", "6"), ("T", "6"), ("9","6"), ("8", "5"), ("7", "5"), ("6", "4"), ("5", "4"), ("4", "3")],
        "off-suited" : [("A", "2"), ("K", "9"), ("Q", "9"), ("J", "9"), ("T", "9")],
        "pairs" : [("A", "2")]
        }
    }

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

def range_of_pairs(high, low):
    i = ranks.index(low)
    many_pairs = []
    while i <= ranks.index(high):
        many_pairs.append(pocket_pairs(ranks[i]))
        i += 1
    return many_pairs

def off_suited(high, low):
    all_high = [h for h in deck.cards if h.rank == high]
    all_low = [l for l in deck.cards if l.rank == low]
    off_suited = []
    for h in all_high:
        for l in all_low:
            if l.suit != h.suit:
                off_suited.append((h, l))
    return off_suited

def range_of_off_suited(high, low):
    i = ranks.index(low)
    j = ranks.index(high)
    many_off = []
    while i < j:
        many_off.append(off_suited(ranks[i],ranks[j]))
        i += 1
    return many_off

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

def range_of_suited(high, low):
    i = ranks.index(low)
    j = ranks.index(high)
    many_suited = []
    while i < j:
        many_suited.append(suited(ranks[i],ranks[j]))
        i += 1
    return many_suited

def build_range(position):
    card_range = []
    hands = []
    
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

def random_hand(hands):
    randint = random.randint(0, len(hands)-1)
    return hands[randint]

for r in ranges:
    print("----")
    print(r)
    for s in random_hand(build_range(r)):
        s.show()
        