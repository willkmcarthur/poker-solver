#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 18:46:16 2021

@author: willmcarthur
"""

from collections import Counter
# from settings import *

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
lowace_ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
straight_string = '23456789TJQKA'
hand_order = ['straight-flush', 'quads', 'full-house', 'flush', 'straight', 'trips', 'two-pair', 'one-pair', 'high-card']

def high_card(cards):
    values = [c.rank for c in cards]
    unique_v = set(values)
    suits = [c.suit for c in cards]
    unique_s = set(suits)
    is_flush = [s for s in unique_s if suits.count(s) >= 5]
    
    if len(unique_v) != len(values):
        return False
    elif is_flush:
        return False
    else:
        return 'high-card', sorted(unique_v, key=lambda unique: ranks.index(unique), reverse = True)[:5]

def one_pair(cards):
    values = [c.rank for c in cards]
    uniques = set(values)
    pairs = [c for c in uniques if values.count(c) == 2]
    if len(pairs) != 1:
        return False
    uniques.remove(pairs[0])
    return 'one-pair', pairs + sorted(uniques, key=lambda unique: ranks.index(unique), reverse = True)[:3]

def two_pair(cards):
    values = [c.rank for c in cards]
    uniques = set(values)
    pairs = [c for c in uniques if values.count(c) == 2]
    if len(pairs) == 2:
        for p in range(len(pairs)):
            uniques.remove(pairs[p])
        return 'two-pair', sorted(pairs, key=lambda pair: ranks.index(pair), reverse = True)[:2] + sorted(uniques, key=lambda unique: ranks.index(unique), reverse = True)[:1]
    elif len(pairs) > 2:
        uniques = [c for c in values if c not in pairs[:2]]
        return 'two-pair', sorted(pairs, key=lambda pair: ranks.index(pair), reverse = True)[:2]  + sorted(uniques, key=lambda unique: ranks.index(unique), reverse = True)[:1]
    else:
        return False

def trips(cards):
    values = [c.rank for c in cards]
    uniques = set(values)
    trips = [c for c in uniques if values.count(c) == 3]
    # if length is greater than 1, its a full_house not double trips, fix later, raise exception later
    if len(trips) != 0:
        for t in range(len(trips)):
            uniques.remove(trips[t])
        return 'trips', sorted(trips, key=lambda trip: ranks.index(trip), reverse = True) + sorted(uniques, key=lambda unique: ranks.index(unique), reverse = True)[:2]
    else:
        return False
    
def straight(cards):
    values = [c.rank for c in cards]
    uniques = set(values)
    if len(uniques) < 5:
        return False
    # lowace straight
    if 'A' in uniques and '2' in uniques and '3' in uniques and '4' in uniques and '5' in uniques and '6' not in uniques:
        straight_cards = sorted(uniques, key=lambda unique: lowace_ranks.index(unique))[:5]
        for c in range(len(straight_cards)):
            uniques.remove(straight_cards[c])
        return 'straight', straight_cards # + sorted(uniques, key=lambda unique: ranks.index(unique), reverse = True)
    # other straight
    else:
        ordered = sorted(uniques, key=lambda unique: ranks.index(unique))
        straight_exists = False
        
        for i in range(len(ordered)-4):
            s = ''.join(o for o in ordered[i:i+5])
            if s in straight_string:
                straight_exists = True
                sr = s
                
        if straight_exists:
            straight_cards = list()
            for i in range(len(sr)):
                straight_cards.append(sr[i])
                uniques.remove(straight_cards[i])
            return 'straight', sorted(straight_cards, key=lambda c: ranks.index(c), reverse=True)
            
        return False
    
def flush(cards):
    suits = [c.suit for c in cards]
    uniques = set(suits)
    flush = [s for s in uniques if suits.count(s) >= 5]
    if len(flush) > 1:
        raise ValueError("Invalid hand")
    elif len(flush) == 1:
        flush_ranks = [c.rank for c in cards if c.suit == flush[0]]
        return 'flush', sorted(flush_ranks, key=lambda fr: ranks.index(fr), reverse = True)[:5]
    else: 
        return False
    

def full_house(cards):
    values = [c.rank for c in cards]
    uniques = set(values)
    trips = [c for c in uniques if values.count(c) == 3]
    pairs = [c for c in uniques if values.count(c) >= 2 and c not in trips]
    if len(trips) == 0 or len(pairs) == 0:
        return False
    else:
        ordered_t = sorted(trips, key=lambda trip: ranks.index(trip), reverse=True)
        if len(ordered_t) > 1:
            for o in ordered_t[1:]:
                ordered_t.remove(o)
        ordered_p = sorted(pairs, key=lambda pair: ranks.index(pair), reverse=True)
        full_house_cards = ordered_t + ordered_p
        return 'full-house', full_house_cards[:2]

def quads(cards):
    values = [c.rank for c in cards]
    uniques = set(values)
    quads = [c for c in uniques if values.count(c) == 4]
    if len(quads) == 0:
        return False
    else:
        for q in quads:
            uniques.remove(q)
        return 'quads', (sorted(quads, key=lambda quad: ranks.index(quad), reverse = True) + sorted(uniques, key=lambda unique: ranks.index(unique), reverse = True))[:2]
    
def straight_flush(cards):
    if not flush(cards):
        return False
    else:
        suits = [c.suit for c in cards]
        uniques = set(suits)
        fc = [s for s in uniques if suits.count(s) >= 5]
        values = [c for c in cards if c.suit == fc[0]]
        if not straight(values):
            return False
        else:
            return 'straight-flush', straight(cards)[1]
    
def determine_hand(cards):
    if valid_hand(cards):
        if straight_flush(cards):
            return straight_flush(cards)
        elif quads(cards):
            return quads(cards)
        elif full_house(cards):
            return full_house(cards)
        elif flush(cards):
            return flush(cards)
        elif straight(cards):
            return straight(cards)
        elif trips(cards):
            return trips(cards)
        elif two_pair(cards):
            return two_pair(cards)
        elif one_pair(cards):
            return one_pair(cards)
        else:
            return high_card(cards)
    else:
        return "That is an invalid hand"
    
def winning_hand(hands):
    wi = hand_order.index(hands[0][0])
    wh = hands[0][1]
    for h in hands:
        if hand_order.index(h[0]) < wi:
            wi = hand_order.index(h[0])
            wh = h[1]
    ties = [h for h in hands if h[0] == hand_order[wi]]
    if len(ties) > 1:
        wh = break_tie(ties)
    return hand_order[wi], wh

def break_tie(hands):
    wi = 0
    wh = hands[0]
    for h,c in hands:
        for i in range(len(c)):
            if ranks.index(c[i]) > wi:
                wi = ranks.index(c[i])
                wh = c
                break
            elif ranks.index(c[i]) == wi:
                continue        
    return wh    

def valid_hand(cards):
    cards_list = []
    for c in cards:
        cards_list.append((c.rank, c.suit))
    c = Counter(cards_list)
    for x in c:
        if c.get(x) > 1:
            return False
    return True
    
    