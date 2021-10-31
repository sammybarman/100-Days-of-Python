# create a text-based treasure island game based on conditionals
'''
flowchart - https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
'''

import os


def treasure():
    print("Welcome to Treasure Island!")
    print("You are a treasure-seeking adventurer on a quest to find the sunken treasure of the island.")
    print("Your mission is to find the treasure!")
    print("You are on an island, do you want to go left or right?")
    direction = input("left or right? : ")
    os.system('clear')

    if direction == "right":
        print("You fell into a hole a died! Play Again?")
        play_again = input("yes or no? : ")
        if play_again == "yes":
            treasure()
        else:
            print("Thanks for playing!")
    elif direction == "left":
        print("You are at a river! Do you wait for the boat or swim across?")
        river = input("wait or swim? : ")
        os.system('clear')
        if river == "swim":
            print("You were attacked by a trout and ferociously eaten alive! Play Again?")
            play_again = input("yes or no? : ")
            if play_again == "yes":
                treasure()
            else:
                print("Thanks for playing!")
        elif river == "wait":
            print("You swam across safely!")
            print("You see three doors in front of you. A red door, a yellow door and a blue door. Which one do you choose?")
            door = input("red, yellow or blue? : ")
            os.system('clear')
            if door == "red":
                print("You were burned by fire! Play Again?")
                play_again = input("yes or no? : ")
                if play_again == "yes":
                    treasure()
                else:
                    print("Thanks for playing!")
            elif door == "yellow":
                print("You won! You escaped out alive. The treasure is your life. Loser")
                print("Thanks for playing!")
            elif door == "blue":
                print(
                    "You were eaten by a half-naked succubus. She bit off your micropenis!!! Play Again?")
                play_again = input("yes or no? : ")
                if play_again == "yes":
                    treasure()
                else:
                    print("Thanks for playing!")
            else:
                print("You tried to be oversmart and entered the wrong input. Fuck you.")
                exit()
        else:
            print("You tried to be oversmart and entered the wrong input. Fuck you.")
            exit()
    else:
        print("You tried to be oversmart and entered the wrong input. Fuck you.")
        exit()


treasure()
