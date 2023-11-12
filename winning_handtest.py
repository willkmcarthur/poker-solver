"""
Created on Sun Feb 13 14:09:07 2022

@author: willmcarthur

This file is contains the main function to test a number of random hands against each other
"""

from hand_analyzer import determine_hand, winning_hand, valid_hand
import random
from poker import Card, Deck
from player import Player

deck = Deck()

# Create and test random hands
def run_tests(deck):
    # Initialize variables for random tests
    compare_hands = []
    num_tests = 10
    i = 0
    while i < num_tests:
        # Create a random hand with 7 cards
        player = Player()
        for s in range(7):
            randint = random.randint(0, 51)
            player.add(deck.cards[randint])
        # Check if the hand is valid
        if valid_hand(player.hand):
            player.show_hand()
            # If it is, determine the hand and add it to the list of hands to compare
            compare_hands.append(determine_hand(player.hand))
            print(determine_hand(player.hand))
            print("----------------------------")
            i+=1
    return compare_hands