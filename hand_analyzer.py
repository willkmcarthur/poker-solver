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
    # Lowace straight only exists if the cards are exactly A, 2, 3, 4, 5
    if 'A' in uniques and '2' in uniques and '3' in uniques and '4' in uniques and '5' in uniques and '6' not in uniques:
        straight_cards = sorted(uniques, key=lambda unique: lowace_ranks.index(unique))[:5]
        # Return the straight
        return 'straight', straight_cards 
    
    # Check for other straights
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
            # Create a list of the cards in the straight
            straight_cards = list()
            for i in range(len(straight_ranks)):
                straight_cards.append(straight_ranks[i])
            # Return the straight
            return 'straight', sorted(straight_cards, key=lambda c: ranks.index(c), reverse=True)
        return False
    
def flush(cards):
    # Find all suits and unique suits
    suits = [card.suit for card in cards]
    uniques = set(suits)
    # Find suits with at least 5 cards
    flush = [suit for suit in uniques if suits.count(suit) >= 5]

    # If there are more than one flush, it's an invalid hand
    if len(flush) > 1:
        raise ValueError("Invalid hand")
    
    # If there is a flush, return it with the highest 5 cards sorted by rank
    elif len(flush) == 1:
        # Find the ranks of the cards with the suit of the flush
        flush_ranks = [card.rank for card in cards if card.suit == flush[0]]
        return 'flush', sorted(flush_ranks, key=lambda fr: ranks.index(fr), reverse = True)[:5]
    else: 
        return False
    

def full_house(cards):
    # Find all values and unique values
    values = [card.rank for card in cards]
    uniques = set(values)
    # Find unique sets of 3 and 2
    trips = [card for card in uniques if values.count(card) == 3]
    pairs = [card for card in uniques if values.count(card) >= 2 and card not in trips]
    
    # For full house, there must be at least one trip and one pair
    if len(trips) == 0 or len(pairs) == 0:
        return False
    
    # If there is more than one trip, we need to find the highest trip
    else:
        ordered_trips = sorted(trips, key=lambda trip: ranks.index(trip), reverse=True)
        # Remove all trips except the highest
        if len(ordered_trips) > 1:
            for o in ordered_trips[1:]:
                ordered_trips.remove(o)
        # If there is more than one pair, we need to find the highest pair
        ordered_pairs = sorted(pairs, key=lambda pair: ranks.index(pair), reverse=True)
        # Build the full house with the highest trip and sorted pairs
        full_house_cards = ordered_trips + ordered_pairs
        # Return the full house by taking the highest trip and first pair in the sorted pairs list
        return 'full-house', full_house_cards[:2]

def quads(cards):
    # Find all values and unique values
    values = [card.rank for card in cards]
    uniques = set(values)
    # Check if there are any quads
    quads = [card for card in uniques if values.count(card) == 4]

    # If there are no quads, it's not a quads hand
    if len(quads) == 0:
        return False
    # If there are multiple quads, it's an invalid hand
    else:
        # Remove cards in the quad from the unique values, so we can find the kicker
        for quad in quads:
            uniques.remove(quad)
        # Return the quad and the highest remaining card by including the remaining uniques sorted by highest rank and only taking the first card
        return 'quads', (sorted(quads, key=lambda quad: ranks.index(quad), reverse = True) + sorted(uniques, key=lambda unique: ranks.index(unique), reverse = True))[:2]
    
def straight_flush(cards):
    # Check for flush
    if not flush(cards):
        return False
    
    # If there is a flush, check for straight
    else:
        # Find the flush suit
        suits = [card.suit for card in cards]
        uniques = set(suits)
        flush_suit = [suit for suit in uniques if suits.count(suit) >= 5]
        # Find the ranks of the cards with the suit of the flush
        values = [card for card in cards if card.suit == flush_suit[0]]

        # Using the ranks of the flush, check for straight
        if not straight(values):
            return False
        # If there is a straight, return the straight flush
        else:
            # The straight function returns a tuple with the type of hand and the cards in the hand
            # We only need the cards in the hand, so we return the second element of the tuple
            return 'straight-flush', straight(cards)[1]
    
def determine_hand(cards):
    # Check for valid hand
    if valid_hand(cards):
        # Check for hands in order of hand strength
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
    
    # If the hand is not valid, raise an exception
    else:
        return "That is an invalid hand"
    
def winning_hand(hands):
    # Set an initial winning hand and index in the hand_order dictionary to the first hand
    # hand_order is sorted from strongest to weakest hand, so the lower the index, the stronger the hand
    winning_index = hand_order.index(hands[0][0])
    winning_hand = hands[0][1]

    # Check each hand against the current winning hand
    for hand in hands:
        # If the hand is stronger than the current winning hand, it becomes the new winning hand
        # We check this by seeing if the index of the hand in the hand_order dictionary is lower than the current winning index
        if hand_order.index(hand[0]) < winning_index:
            winning_index = hand_order.index(hand[0])
            winning_hand = hand[1]

    # Check for ties
    ties = [hand for hand in hands if hand[0] == hand_order[winning_index]]
    # If there is a tie, break it using kickers and other tie breakers
    if len(ties) > 1:
        print("Tie Breaker between " + str(len(ties)) + " " + str(hand_order[winning_index]) + " hands.")
        winning_hand = break_tie(ties)
    
    # Return the winning hand and the type of hand
    print("The winning hand is")
    return hand_order[winning_index], winning_hand

def break_tie(hands):
    # The winning index and winning hand is now scoped to just the hands that are tied
    # Set the initial winning index and winning hand to the first hand in the list and the first card in the hand
    # This is because the returns of the hand functions are tuples with a sorted list from highest to lowest rank
    # In poker, if the highest card in one hand is higher than the highest card in another hand, the first hand wins the tie break
    winning_index = 0
    winning_hand = hands[0]
    # If the tie is between straights, we need to check for a lowace straight
    if winning_hand[0] == 'straight':
            i = 0
            for hand in hands:
                # Check for exactly A, 2, 3, 4, 5
                if hand[1][0] == 'A' and hand[1][4] == '5':
                    # Set the winning index to 4 since 5 is the highest card in the straight
                    winning_index = 4
                    # Set the winning hand to the lowace straight
                    winning_hand = hand
                    # Remove the lowace straight from the list of hands to check
                    hands.pop(i)
                i += 1
    
    # Check each hand leftover after the lowace straight check to see if it has a higher card than the current winning hand
    # Remeber the hands are tuples with the name of the hand and the cards in the hand
    for hand, cards in hands:
        # Check each card in the hand to see if it has a higher rank than the current winning hand
        for i in range(len(cards)):
            # If the card has a higher rank, it becomes the new winning hand, and we go to the next hand in the tie break
            if ranks.index(cards[i]) > winning_index:
                winning_index = ranks.index(cards[i])
                winning_hand = cards
                break
            # If the card matches rank, we go to the next card in the hand
            elif ranks.index(cards[i]) == winning_index:
                continue       

    # Return the winning hand 
    return winning_hand    

def valid_hand(cards):
    # Check for duplicate cards
    cards_list = []
    for card in cards:
        cards_list.append((card.rank, card.suit))
    card = Counter(cards_list)
    for x in card:
        if card.get(x) > 1:
            return False
    return True
    
    