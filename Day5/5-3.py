# write a program that takes a list of numbers and only adds the even numbers


def three(numbers):
    sum = 0
    for number in numbers:
        if number % 2 == 0:
            sum += number

    return sum


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The sum of even numbers is - ", three(numbers))
