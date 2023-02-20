'''
write a program to calculate the amount of paint cans needed to paint a wall of length*width
1 can of paint can cover 5sq meters of the wall
round up cans to the nearest integer
'''

import math


def one(height, width):
    area = height*width
    cans = math.ceil((area/5))
    return cans


def main():
    height = int(input("Enter the height of the wall (in sq meters): "))
    width = int(input("Enter the width of the wall (in sq meters): "))
    print(
        f"You will need {one(height, width)} cans of paint to paint the wall.")


main()
