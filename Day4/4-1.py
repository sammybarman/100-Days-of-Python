# write a program that generates a random heads or tails

import random


def one():
    return random.choice(['Heads', 'Tails'])


h_t = one()
print(h_t)
