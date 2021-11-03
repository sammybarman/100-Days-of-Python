# given a list of scores, return the highest score. Can't use max()

def two(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number

    return max


numbers = [78, 65, 89, 55, 91, 64, 89]
print("The highest score in the class is : ", two(numbers))
