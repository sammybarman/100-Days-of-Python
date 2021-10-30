# a program to calculate the total tip for a meal
import math


def two():
    print("Welcome to the tip calculator.")

    bill = float(input("What was the total bill? = $"))
    num_people = float(input("How many people will split the bill? - "))
    tip_percent = float(input("What percent would you like to tip? - "))

    total_bill = bill + (bill * (tip_percent / 100))
    each_person = total_bill / num_people
    each_person = str(round(each_person, 2))
    # the round function operates as follows - round(number, decimal_places)
    print("Each person should pay: $", each_person)
    # can also use python 3.6+ f-strings to print the above line
    # print(f"Each person should pay: ${:0.2f}.format(each_person)") where f indicates f-string formatting, and 0.2f indicates 2 decimal places. 0 indicates sign-aware zero padding for numeric types, and the : indicates the start of a format specifier.
    # .2 sets the precision to 2 decimal places.


two()
