# write a program to add the digits of a given number
# easiest method in python is to convert number to string, then iterate through each character and add them up
# another method is to use the modulo operator %. Divide the number by 10 and add the remainder to the sum. Repeat this process until the number is 0.

def two(n):

    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)

    return sum


try:
    number = int(input("Enter a number - "))
    print("The sum of digits in the number is - ", two(number))
except:
    print("Please enter a valid integer")
