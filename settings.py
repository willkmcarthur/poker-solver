#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 17:26:54 2022

@author: willmcarthur
"""

from poker import Deck, Player, Card

deck = Deck()

test = [
        [Card("Clubs","2"), Card("Hearts","2"), Card("Clubs","7"), Card("Clubs","K"), Card("Diamonds","5"), Card("Diamonds","6"), Card("Diamonds","9")],
        [Card("Diamonds","2"), Card("Spades","2"), Card("Clubs","3"), Card("Diamonds","4"), Card("Diamonds","5"), Card("Clubs","9"), Card("Diamonds","7")],
        [Card("Diamonds","2"), Card("Spades","2"), Card("Clubs","5"), Card("Diamonds","4"), Card("Diamonds","7")],
        [Card("Diamonds","2"), Card("Spades","2"), Card("Clubs","5"), Card("Diamonds","5"), Card("Diamonds","7"), Card("Spades","7"), Card("Clubs","A")],
        [Card("Diamonds","2"), Card("Spades","2"), Card("Clubs","2"), Card("Diamonds","3"), Card("Diamonds","7"), Card("Spades","7"), Card("Clubs","A")],
        [Card("Diamonds","K"), Card("Spades","3"), Card("Clubs","4"), Card("Diamonds","5"), Card("Diamonds","2"), Card("Spades","6"), Card("Clubs","7")],
        [Card("Diamonds","K"), Card("Spades","3"), Card("Clubs","4"), Card("Diamonds","5"), Card("Diamonds","2"), Card("Spades","6"), Card("Clubs","7")],
        [Card("Diamonds","K"), Card("Diamonds","5"), Card("Diamonds","Q"), Card("Spades","K"), Card("Clubs","7"), Card("Diamonds","J"), Card("Diamonds","T")],
        [Card("Diamonds","K"), Card("Diamonds","Q"), Card("Diamonds","6"), Card("Spades","J"), Card("Clubs","9"), Card("Diamonds","T"), Card("Diamonds","9")],
        [Card("Diamonds","K"), Card("Diamonds","2"), Card("Diamonds","3"), Card("Spades","K"), Card("Clubs","9"), Card("Diamonds","Q"), Card("Diamonds","T")],
        [Card("Diamonds","K"), Card("Diamonds","A"), Card("Diamonds","Q"), Card("Spades","K"), Card("Clubs","9"), Card("Diamonds","J"), Card("Diamonds","T")],
        [Card("Diamonds","6"), Card("Hearts","6"), Card("Diamonds","A"), Card("Spades","6"), Card("Clubs","T"), Card("Diamonds","5"), Card("Diamonds","Q")],
        ]

hand_order = ['straight-flush', 'quads', 'full-house', 'flush', 'straight', 'trips', 'two-pair', 'one-pair', 'high-card']

suits = ["Diamonds", "Hearts", "Clubs", "Spades"]

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

lowace_ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

straight_string = '23456789TJQKA'

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
