#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 11:02:00 2021

@author: willmcarthur

Main Testing file for the poker project
"""

from hand_analyzer import determine_hand, winning_hand, valid_hand
from winning_handtest import run_tests
import random
from poker import Card, Deck
from player import Player

# Manually created tests
test = [
        # [Card("Clubs","2"), Card("Hearts","2"), Card("Clubs","7"), Card("Clubs","K"), Card("Diamonds","5"), Card("Diamonds","6"), Card("Diamonds","9")],
        # [Card("Diamonds","2"), Card("Spades","2"), Card("Clubs","3"), Card("Diamonds","4"), Card("Diamonds","5"), Card("Clubs","9"), Card("Diamonds","7")],
        # [Card("Diamonds","2"), Card("Spades","2"), Card("Clubs","5"), Card("Diamonds","4"), Card("Diamonds","7")],
        # [Card("Diamonds","2"), Card("Spades","2"), Card("Clubs","5"), Card("Diamonds","5"), Card("Diamonds","7"), Card("Spades","7"), Card("Clubs","A")],
        # [Card("Diamonds","2"), Card("Spades","2"), Card("Clubs","2"), Card("Diamonds","3"), Card("Diamonds","7"), Card("Spades","7"), Card("Clubs","A")],
        # Straight Tests
        [Card("Diamonds","A"), Card("Spades","3"), Card("Clubs","4"), Card("Diamonds","5"), Card("Diamonds","2"), Card("Spades","6"), Card("Clubs","7")],
        [Card("Diamonds","K"), Card("Spades","Q"), Card("Clubs","J"), Card("Diamonds","T"), Card("Diamonds","9"), Card("Spades","6"), Card("Clubs","7")],
        [Card("Diamonds","A"), Card("Spades","3"), Card("Clubs","4"), Card("Diamonds","5"), Card("Diamonds","2"), Card("Spades","8"), Card("Clubs","9")],
        [Card("Diamonds","A"), Card("Spades","K"), Card("Clubs","Q"), Card("Diamonds","J"), Card("Diamonds","T"), Card("Spades","6"), Card("Clubs","7")],
        [Card("Diamonds","A"), Card("Spades","2"), Card("Clubs","3"), Card("Diamonds","4"), Card("Diamonds","5"), Card("Spades","6"), Card("Clubs","8")],
        # [Card("Diamonds","K"), Card("Diamonds","5"), Card("Diamonds","Q"), Card("Spades","K"), Card("Clubs","7"), Card("Diamonds","J"), Card("Diamonds","T")],
        # [Card("Diamonds","K"), Card("Diamonds","Q"), Card("Diamonds","6"), Card("Spades","J"), Card("Clubs","9"), Card("Diamonds","T"), Card("Diamonds","9")],
        # [Card("Diamonds","K"), Card("Diamonds","2"), Card("Diamonds","3"), Card("Spades","K"), Card("Clubs","9"), Card("Diamonds","Q"), Card("Diamonds","T")],
        # [Card("Diamonds","K"), Card("Diamonds","A"), Card("Diamonds","Q"), Card("Spades","K"), Card("Clubs","9"), Card("Diamonds","J"), Card("Diamonds","T")],
        # [Card("Diamonds","6"), Card("Hearts","6"), Card("Diamonds","A"), Card("Spades","6"), Card("Clubs","T"), Card("Diamonds","5"), Card("Diamonds","Q")],
        ]
deck = Deck()

# Check the manual tests
compare_tests = []
for t in test:
    print(determine_hand(t))
    compare_tests.append(determine_hand(t))
    print("----------------------------")
print('The winning hand is')
print(winning_hand(compare_tests))

# Run the tests from the winning_handtest.py file and print the results
print(winning_hand(run_tests(deck)))
