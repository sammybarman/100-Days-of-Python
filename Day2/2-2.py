# write a program to create a bmi calculator based on height and input


def three():

    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kg: "))

    bmi = weight / (height ** 2)
    return bmi


result = three()
print("Your BMI is - ", int(result))
