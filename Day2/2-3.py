#life in weeks
# write a program that takes your current age and display the number of days,weeks and months you have left to live if you live upto 90
# round up answers to nearest whole number

import math


def three():

    age = int(input("Enter your age: "))
    days = math.ceil(age * 365)
    weeks = math.ceil(age * 52)
    months = math.ceil(age * 12)
    print(f"You have lived for {days} days, {weeks} weeks, {months} months")

    days_left = math.ceil((90 - age) * 365)
    weeks_left = math.ceil((90 - age) * 52)
    months_left = math.ceil((90 - age) * 12)
    print(
        f"You have {days_left} days, {weeks_left} weeks, {months_left} months left to live")


three()
