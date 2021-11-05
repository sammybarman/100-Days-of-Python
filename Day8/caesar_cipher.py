# create a program to encode and decode messages using the casear cipher
# chr - converts a number to a character relevant to the ASCII table
# ord - converts a character to an ASCII number
# isalpha - checks if a character is a letter

import os

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


def encode(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                char = chr((ord(char)+shift - 65) % 26 + 65)
            else:
                char = chr((ord(char)+shift - 97) % 26 + 97)
            result += char
        else:
            result += char

    return result


def decode(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                char = chr((ord(char)-shift - 65) % 26 + 65)
            else:
                char = chr((ord(char)-shift - 97) % 26 + 97)
            result += char
        else:
            result += char

    return result


def main():
    print(logo)
    print("Would you like to encode or decode a message?")
    choice = input("Enter 'e' to encode or 'd' to decode: ")

    try:
        if choice == 'e':
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            print("Your encrypted message is - ")
            print(encode(message, shift))

        elif choice == 'd':
            message = input("Enter your encrypted message: ")
            shift = int(input("Enter the shift value: "))
            print("Your decrypted text is - ")
            print(decode(message, shift))
        else:
            print("Please enter a valid choice.")

    except:
        print("Please enter a valid choice.")

    print("Would you like to go again?")
    again = input("Enter 'y' to go again or 'n' to quit: ")
    try:
        if again == 'y':
            os.system('clear')
            main()
        elif again == 'n':
            os.system('clear')
            print("Goodbye")
        else:
            print("Please enter a valid choice.")
    except:
        print("Please enter a valid choice.")


main()
