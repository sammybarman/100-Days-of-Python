# banker roulette
'''
create a program that selects a name from a list of names. That person needs to pay the bill. can't use random.choice
'''

import random


def two():
    names = ['John', 'Bob', 'Mary', 'Sue', 'Joe', 'Paul']
    l = len(names)
    i = random.randint(0, l-1)
    pay = names[i]
    print(f"The bill needs to be paid by {pay}")


two()
