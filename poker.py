#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 10:51:55 2021

@author: willmcarthur

This file contains the classes for the poker project
"""
    
import random
from settings import suits, ranks
from ranges import build_range, random_hand

# Class for the deck of cards
class Deck:
    # Initialize the deck
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()
    # Build the deck with all 52 cards using suits and ranks from settings.py
    def build(self):
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s,r))
    # Show the deck
    def show(self):
        for c in self.cards:
            c.show()
    # Shuffle the deck
    def shuffle(self):
        # Randomly swap cards in the deck 
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    # Draw a card from the deck by removing the last card in the deck
    def draw_card(self):
        return self.cards.pop()     

# Class for a card
class Card:
    # Initialize the card with a suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    # Show the card
    def show(self):
        print ("{} of {}".format(self.rank, self.suit))

# Class for a player
# Need to add error handling for if the arguments passed to the player constructor are out of order
# Or if the arguments passed to the player constructor are not valid
class Player:

    # Initialize the player with a hand, position, and starting stack
    def __init__(self, *inp):
        # If 2 arguments are passed to the player constructor, create a player with a position and starting stack and empty hand
        if len(inp) == 2:
            self.table_player(inp[0], inp[1])
        # Need to add other cases for number of arugments passed to the player constructor
        else:
            self.create()

    # Create a player with an empty hand, position, and starting stack
    def create(self):
        self.hand = []
        self.position = 0
        self.stack = 0
    
    # If the player is a table player, set the position and starting stack
    def table_player(self, position, starting_stack):
        self.hand = []
        self.position = position
        self.stack = starting_stack
    
    # Create a hand for the player based on their position and range
    def hand_in_range(self, position):
        self.position = position
        self.hand = random_hand(build_range(position))
    
    # Add a card to the player's hand
    def add(self, card):
        self.hand.append(card)
    
    # Draw a card from the deck and add it to the player's hand
    def draw(self, deck):
        self.hand.append(deck.draw_card())
    
    # Show the player's hand
    def show_hand(self):
        for i in range(len(self.hand)):
            print ("{} of {}".format(self.hand[i].rank, self.hand[i].suit))

# Should add a Player Hand Constructor that takes a position and returns a hand
# Should add a Player Constructor that takes two cards and returns a player
# Should add a Table Constructor that takes a list of players and returns a table

# Class for a round of poker
class Round():
    
    # Initialize the round by setting the "stage" to 0
    def __init__(self):
        self.stage = 0
    
    # Increment the stage of the round, without exceeding 3
    def next_stage(self):
        self.stage = (self.stage + 1) % 4
    
    # The idea with the below code is that we can initialize a round
    # with a list of players and a deck, and then as the rounds progress
    # we can update the players' hands and the table cards

    # def __init__(self, num_players, deck):
    #     self.players = []
    #     for p in range(0, num_players-1, 1):
    #         self.players.append(Player())
    #         for c in range(0,2,1):
    #             self.players[p].draw(deck)
    
    # def show_hands(self):
    #     for i in range(0, len(self.players), 1):
    #         print("Player {}:".format(i+1))
    #         self.players[i].show_hand()
    #         print("---------")

# Class for a pot
class Pot():
    # Initialize the pot
    def __init__(self):
        amount = 0
        bb = 0
        smb = 0
        bet = 0
        raise_diff = 0
        min_raise = 2*raise_diff + bet
        winner = None
    
    # Function to determine if a bet is valid based on the current bet, raise difference, and minimum raise
    def valid_bet(self, bet):
        if bet >= self.big_blind:
            if bet >= self.min_raise or bet == self.bet:
                return True
        return False
    
    # Set the blinds for the pot
    def set_blinds(self, big, small):
        self.bb = big
        self.smb= small
            
# def current_hand(player_hand, table_cards):
#     cards = player_hand + table_cards
    


