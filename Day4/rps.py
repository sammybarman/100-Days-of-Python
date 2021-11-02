# write a program that plays rock, paper, scissors with you

import random
import os


def rps():
    s = [1, 2, 3]
    while True:
        print("Please choose one of the following:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")
        try:
            a = int(input("Please choose an option: "))
            b = random.choice(s)
            if a == b:
                print("It's a tie!")

            elif a == 1:
                if b == 2:
                    print("Opponent choose Paper")
                    print("You lose!")

                else:
                    print("Opponent choose Scissors")
                    print("You win!")

            elif a == 2:
                if b == 3:
                    print("Opponent choose Scissors")
                    print("You lose!")

                else:
                    print("Opponent choose Rock")
                    print("You win!")

            elif a == 3:
                if b == 1:
                    print("Opponent choose Rock")
                    print("You lose!")

                else:
                    print("Opponent choose Paper")
                    print("You win!")

            elif a == 4:
                print("Thanks for Playing!")
                break
            else:
                print("Please choose a valid option!")
        except:
            print("Please enter a valid choice!!")


print("Welcome to Rock, Paper, Scissors!")
rps()
