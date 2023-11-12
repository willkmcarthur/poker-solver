from ranges import random_hand, build_range
from settings import ranges

for r in ranges:
    print("----")
    print("A random hand in the " + r + " range:")
    for s in random_hand(build_range(r)):
        s.show()