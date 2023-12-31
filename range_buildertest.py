"""
@author: willmcarthur

This file tests our range building functions
"""
from poker import Deck
from ranges import build_range, random_hand, pocket_pairs, range_of_pairs, suited, range_of_suited, off_suited, range_of_off_suited, ranges
from settings import suits, ranks, lowace_ranks, straight_string, hand_order

# Test the range building functions by printing the ranges for each position
for r in ranges:
    print("----")
    print(r)
    for s in (build_range(r)):
        for c in s:
            c.show()
        print("----")