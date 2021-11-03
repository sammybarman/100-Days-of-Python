# create a program that generates passwords for you
'''
Asks for number of letters
Asks for number of symbols
Asks for how many numbers 
Generates a password 
'''
import random

characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
              "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [".", "$", "/", "|", "?", "!", "@", "#", "%", "^", "&", "*",
           "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ":", ";", "'", "<", ">", ",", ".", " "]


def password_gen():

    a = int(input("How many characters? "))
    b = int(input("How many symbols? "))
    c = int(input("How many numbers? "))

    char_len = a-b-c
    empty_list = []
    password = ""

    for i in range(0, char_len):
        empty_list.append(random.choice(characters))

    for i in range(0, b):
        empty_list.append(random.choice(symbols))

    for i in range(0, c):
        empty_list.append(random.choice(numbers))

    for i in range(0, a):
        password = password + random.choice(empty_list)

    return password


print("Your password is -", password_gen())
