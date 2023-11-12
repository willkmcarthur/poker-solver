#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 09:44:27 2022

@author: willmcarthur

This file is for creating a game loop for the poker game
"""

# Initialize players & position
from poker import Player, Deck, Round, Pot

print("Please enter the number of players: ")
num_players = int(input())
print("Now enter the starting stack size: ")
starting_stack = int(input())
print("And finally the initial small blind amount, the big blind will be double this amount: ")
smb = int(input())

players = []
for i in range(num_players):
    players += [Player(i, starting_stack)]

deck = Deck()
btn_pos = 0
smb = (btn_pos + 1) % num_players
bb = (btn_pos + 2) % num_players



# r1 = Round()
# print("r1 stage is {}".format(r1.stage))
# r1.next_stage()
# print("r1 stage is {}".format(r1.stage))
# r1.next_stage()
# print("r1 stage is {}".format(r1.stage))
# r1.next_stage()
# print("r1 stage is {}".format(r1.stage))
# r1.next_stage()
# print("r1 stage is {}".format(r1.stage))

# Start game
game_over = False
while not game_over:
    
    # Deal player hands
    for i in range(2):
        for p in players:
            p.draw(deck)
            
    # Init pot
    pot = Pot()
    pot.set_blinds(2*smb, smb)
    
    # Init round
    r = Round()
    round_over = False
    while not round_over:
        pos_to_act = btn_pos + 1
        
        # Pre-flop loop
        if r.stage == 0:
            pos_to_act = bb + 1
            print("It's Player {}'s turn.".format(pos_to_act))
        
        # Post-flop loop
        elif r.stage == 1:
            break
        
        # Turn loop
        elif r.stage == 2:
            break
        
        # River loop
        elif r.stage == 3:
            break
        
            
        
        break
        r.next_stage()
        if r.stage == 0:
            round_over = True
            btn_pos += 1
            break
        
    # Before looping, change blinds?
    

print("I will now deal cards to {} players...".format(num_players))

for i in range(2):
    for p in players:
        p.draw(deck)

for p in players:
    print("----")
    for c in p.hand:
        c.show()