# create a program that calculates the BMI of a person given their weight and height and interpret the result
'''
<18.5 - Underweight
18.5 - 25 - Normal
25 - 30 - Overweight
30 - 35 - Obese
Above 35 - Clinically obese
'''


def two():
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
        bmi = round(weight / (height ** 2), 2)
        print("Your BMI is: ", bmi)

        if bmi < 18.5:
            print("You are underweight")
        elif bmi < 25:
            print("You have a normal weight")
        elif bmi < 30:
            print("You are overweight")
        elif bmi < 35:
            print("You are obese")
        else:
            print("You are clinically obese")

    except:
        print("Enter correct values!")


two()
