# create a pizza order program. Based on users order, output their final bill
'''
Small Pizza = 15$
Medium Pizza = 20$
Large Pizza = 25$

Pepperoni for Small Pizza = +2$
Pepperoni for Medium/Large Pizza = +3$

Extra Cheese for any size pizza = +1$

'''


def four():

    print("Welcome to Python Pizza!")
    print("Please select your pizza size:")
    print("1. Small")
    print("2. Medium")
    print("3. Large")
    print("4. Exit")
    size = int(input("Please select your pizza size: "))
    if size != 4:
        bill = 0
        print("Would you like extra pepperoni?")
        pepperoni = input("Please enter y or n: ")
        print("Would you like extra chess?")
        cheese = input("Please enter y or n: ")

        if size == 1:
            bill = bill + 15
            if pepperoni == "y":
                bill = bill + 3
            if cheese == "y":
                bill = bill + 1
        elif size == 2:
            bill = bill + 20
            if pepperoni == "y":
                bill = bill + 2
            if cheese == "y":
                bill = bill + 1
        elif size == 3:
            bill = bill + 25
            if pepperoni == "y":
                bill = bill + 3
            if cheese == "y":
                bill = bill + 1
    elif size == 4:
        print("Sorry to see you leave!")
        exit()
    else:
        print("We dont have that pizza size!")
        exit()

    print(f"Your bill is: ${bill}")


four()
