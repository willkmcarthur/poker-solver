from hand_analyzer import determine_hand, winning_hand, valid_hand
import random
from poker import Card, Player, Deck

deck = Deck()

compare_hands = []

def run_tests(deck):
    i = 0
    while i < 10:
        player = Player()
        for s in range(7):
            randint = random.randint(0, 51)
            player.add(deck.cards[randint])
        if valid_hand(player.hand):
            player.show_hand()
            compare_hands.append(determine_hand(player.hand))
            print(determine_hand(player.hand))
            print("----------------------------")
            i+=1
        
run_tests(deck)
print('The winning hand is')
print(winning_hand(compare_hands))