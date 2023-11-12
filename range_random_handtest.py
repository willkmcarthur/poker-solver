from ranges import random_hand, build_range
from settings import ranges

# Test the random hand function by printing a random hand from each range
for r in ranges:
    print("----")
    print("A random hand in the " + r + " range:")
    for s in random_hand(build_range(r)):
        s.show()