
from ranges import build_range, random_hand

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
