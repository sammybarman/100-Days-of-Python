'''
write a program to check if a given number is prime or not
'''


def two(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def main():
    print("Enter an number to check wether it's prime or not")
    number = int(input("Number - "))
    isPrime = two(number)
    if isPrime == True:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


main()
