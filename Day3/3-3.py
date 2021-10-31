# write a program to check wether a given year is a leap year or not
'''
A year is a leap year if it is divisible by 4 but not by 100, or it is divisible by 400.
'''


def three():
    try:
        year = int(input("Enter the year you want to check - "))

        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("The year is a leap year")
        else:
            print("The year is not a leap year")
    except:
        print("Enter a valid year")


three()
