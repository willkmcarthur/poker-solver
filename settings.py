#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 17:26:54 2022

@author: willmcarthur

This file contains constants for the poker project
"""
# hand_order is the order of hands from best to worst
hand_order = ['straight-flush', 'quads', 'full-house', 'flush', 'straight', 'trips', 'two-pair', 'one-pair', 'high-card']
# suits is a list of all suits
suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
# ranks is a list of all ranks from lowest to highest
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
# lowace_ranks is a list of all ranks from lowest to highest with Ace as the lowest card
# This is mainly used for determining straights
lowace_ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
# straight_string is a string of all ranks from lowest to highest, used for determining straights
straight_string = '23456789TJQKA'
# lowace_straight_string is a string of all ranks from lowest to highest with Ace as the lowest card, used for determining straights
lowace_straight_string = 'A23456789TJQK'

# ranges is a dictionary of ranges for each position
# The ranges are broken down into suited, off-suited, and pairs
# Where suited is a list of all suited hands for that position, i.e. (A, T) means all suited hands with an Ace and a Ten
# off-suited is a list of all off-suited hands for that position, using a low and high card i.e. (A, T) means all off-suited hand combinations between Ace and Ten
# i.e. (A, T) in off-suited means (A, T), (A, J), (A, Q), (A, K), (K, T), (K, Q), (K, J), (Q, T), (Q, J), (J, T)
# pairs is a list of all pairs for that position, using a low and high card i.e. (A, T) means all pairs between Ace and Ten
# i.e. (A, T) in pairs means (A, A), (K, K), (Q, Q), (J, J), (T, T)
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
