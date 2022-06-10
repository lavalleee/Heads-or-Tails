##This is a small program to help you make extremely tough decisions..

import random

print(f"This is going to help you make a tough decision very quickly.\n")

HeadsNTails = random.randint(1, 2)
if HeadsNTails == 1:
    print("The answer is Heads.")
else:
    print("The answer is Tails.")
