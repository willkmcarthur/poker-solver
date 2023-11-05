#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 18:46:16 2021

@author: willmcarthur

This file contains the functions for determining the type of hand a player has
"""

from collections import Counter
from settings import ranks, lowace_ranks, straight_string, hand_order


def high_card(cards):

    # Find all values, unique values, suits, and unique suits
    values = [card.rank for card in cards]
    unique_values = set(values)
    suits = [card.suit for card in cards]
    unique_suits = set(suits)

    # Check for flush
    is_flush = [s for s in unique_suits if suits.count(s) >= 5]
    
    # If there are duplicate values, it's not a high card hand
    if len(unique_values) != len(values):
        return False
    
    # If all cards have the same suit, it's not a high card hand
    elif is_flush:
        return False
    
    # Otherwise, it's a high card hand
    # Return the high card and sorted list of the next four highest cards
    else:
        return 'high-card', sorted(unique_values, key=lambda unique: ranks.index(unique), reverse = True)[:5]

def one_pair(cards):

    # Find all values and unique values
    values = [card.rank for card in cards]
    uniques = set(values)

    # Find all pairs using unique values and list the ranks of the pairs
    pairs = [rank for rank in uniques if values.count(rank) == 2]

    # If there is more than one pair, it's not a one pair hand
    if len(pairs) != 1:
        return False
    
    # Otherwise, it's a one pair hand
    # Remove the pair from the unique values and sort the remaining cards by highest rank
    uniques.remove(pairs[0])
    return 'one-pair', pairs + sorted(uniques, key=lambda unique: ranks.index(unique), reverse = True)[:3]

def two_pair(cards):

    # Find all values and unique values
    values = [card.rank for card in cards]
    uniques = set(values)

    # Find all pairs using unique values and list the ranks of the pairs
    pairs = [rank for rank in uniques if values.count(rank) == 2]

    # If there are exactly two pairs, it's a two pair hand
    if len(pairs) == 2:
        for p in range(len(pairs)):
            uniques.remove(pairs[p])
        # Return the two pairs sorted by highest rank and the highest remaining card
        return 'two-pair', sorted(pairs, key=lambda pair: ranks.index(pair), reverse = True)[:2] + sorted(uniques, key=lambda unique: ranks.index(unique), reverse = True)[:1]
    
    # If there are more than two pairs, return the two highest pairs and the highest remaining card
    elif len(pairs) > 2:
        uniques = [card for card in values if card not in pairs[:2]]
        return 'two-pair', sorted(pairs, key=lambda pair: ranks.index(pair), reverse = True)[:2]  + sorted(uniques, key=lambda unique: ranks.index(unique), reverse = True)[:1]
    
    # Otherwise, it's not a two pair hand
    else:
        return False

def trips(cards):

    # Find all values and unique values
    values = [card.rank for card in cards]
    uniques = set(values)

    # Find all trips using unique values and list the ranks of the trips
    trips = [card for card in uniques if values.count(card) == 3]

    # If length is greater than 1, its a full_house not double trips, fix later, raise exception later
    # If the trips array is not empty, it's a trips hand
    if len(trips) != 0:
        # Remove the trips from the unique values and sort the remaining cards by highest rank
        for trip in range(len(trips)):
            uniques.remove(trips[trip])
        # Return the trips and the two highest remaining cards
        return 'trips', sorted(trips, key=lambda trip: ranks.index(trip), reverse = True) + sorted(uniques, key=lambda unique: ranks.index(unique), reverse = True)[:2]
    
    # Otherwise, it's not a trips hand
    else:
        return False
    
def straight(cards):
    
    # Find all values and unique values
    values = [card.rank for card in cards]
    uniques = set(values)

    # If there are less than 5 unique values, it's not a straight
    if len(uniques) < 5:
        return False
    
    # Check for straight with low ace
    if 'A' in uniques and '2' in uniques and '3' in uniques and '4' in uniques and '5' in uniques and '6' not in uniques:
        straight_cards = sorted(uniques, key=lambda unique: lowace_ranks.index(unique))[:5]
        for c in range(len(straight_cards)):
            uniques.remove(straight_cards[c])
        # Return the straight
        return 'straight', straight_cards 
    
    # Check for straight with high ace
    else:
        # Order the cards by rank, there may be up to 7 cards
        ordered = sorted(uniques, key=lambda unique: ranks.index(unique))
        # Check for straight
        straight_exists = False
        # There has to be at least 4 cards left in the ordered list to have a straight
        # i.e. if the cards are 2, 4, 6, 8, 9, 10, 11
        # Once the loop gets to 8, there are not enough cards left to have a straight
        for i in range(len(ordered)-4):
            # Build a string of the next 5 cards to test against the straight_string constant
            string_test = ''.join(rank for rank in ordered[i:i+5])
            if string_test in straight_string:
                straight_exists = True
                # Store each version of the straight in a new variable
                # This is to account for the possibility of multiple straights
                # Each time a new string is found with a higher lowest card, it replaces the previous string
                straight_ranks = string_test
                
        if straight_exists:
            straight_cards = list()
            for i in range(len(straight_ranks)):
                straight_cards.append(straight_ranks[i])
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
        print("Tie Breaker between " + str(len(ties)) + " " + str(hand_order[wi]) + " hands.")
        wh = break_tie(ties)
    return hand_order[wi], wh

def break_tie(hands):
    wi = 0
    wh = hands[0]
    # If the tie is between straights, we need to check for a lowace straight
    if wh[0] == 'straight':
            i = 0
            for hand in hands:
                if hand[1][0] == 'A' and hand[1][4] == '5':
                    wi = 4
                    wh = hand
                    hands.pop(i)
                i += 1
    for hand,card in hands:
        for i in range(len(card)):
            if ranks.index(card[i]) > wi:
                wi = ranks.index(card[i])
                wh = card
                break
            elif ranks.index(card[i]) == wi:
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
    
    