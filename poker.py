#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 10:51:55 2021

@author: willmcarthur
"""
    
import random
# from ranges import build_range, random_hand

suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()
    
    def build(self):
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s,r))
                
    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def draw_card(self):
        return self.cards.pop()     

        
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def getSuit(self, rank):
        return self.suit
    
    def show(self):
        print ("{} of {}".format(self.rank, self.suit))

class Player:
    
    def __init__(self, *inp):
  
        if len(inp) == 2:
            self.table_player(inp[0], inp[1])
  
        else:
            self.create()
    
    def create(self):
        self.hand = []
        self.position = 0
        self.stack = 0
    
    # Need to add error handling for if the arguments passed to the player constructor are out of order
    # def table_player(self, position, starting_stack):
    #     self.hand = []
    #     self.position = position
    #     self.stack = starting_stack
    
    # def hand_in_range(self, position):
    #     self.position = position
    #     self.hand = random_hand(build_range(position))
    
    def add(self, card):
        self.hand.append(card)
    
    def draw(self, deck):
        self.hand.append(deck.draw_card())
    
    def show_hand(self):
        for i in range(len(self.hand)):
            print ("{} of {}".format(self.hand[i].rank, self.hand[i].suit))

class Round():
    
    def __init__(self):
        self.stage = 0
    
    def next_stage(self):
        self.stage = (self.stage + 1) % 4
    
    # def __init__(self, num_players, deck):
    #     self.players = []
    #     for p in range(0, num_players-1, 1):
    #         self.players.append(Player())
    #         for c in range(0,2,1):
    #             self.players[p].draw(deck)
            
    def show_hands(self):
        for i in range(0, len(self.players), 1):
            print("Player {}:".format(i+1))
            self.players[i].show_hand()
            print("---------")
            
class Pot():
    
    def __init__(self):
        amount = 0
        bb = 0
        smb = 0
        bet = 0
        raise_diff = 0
        min_raise = 2*raise_diff + bet
        winner = None
        
    def valid_bet(self, bet):
        if bet >= self.big_blind:
            if bet >= self.min_raise or bet == self.bet:
                return True
        return False
    
    def set_blinds(self, big, small):
        self.bb = big
        self.smb= small
            
# def current_hand(player_hand, table_cards):
#     cards = player_hand + table_cards
    


