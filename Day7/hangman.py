# create a hangman game
from random_words import RandomWords
import os
# a python module that generates random words

emoji = ['''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''', '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''']


def hangman(word, word_l):

    life = 6
    i = 5
    ans = ["_"]*len(word)
    print("Welcome to Hangman!")
    logo = ''' 
    _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                    |___/    '''

    print(logo)
    print(emoji[6])
    while life > 0 and "_" in ans:
        print("You have {} lives left".format(life))
        if ans == word:
            print("You win!")
            break
        guess = input("Guess a letter: ").lower()
        if guess in word:
            print("You have guessed correctly!")
            while guess in word:
                index = word.index(guess)
                ans[index] = guess
                word[index] = "_"
            print("".join(ans))
        else:
            life -= 1
            print("You have guessed incorrectly!")
            print(emoji[i])
            i -= 1

    if life == 0:
        print("You lose!")
        print("The word was {}".format(word_l))

    print("Play Again?")
    play_again = input("Y/N: ").lower()
    try:
        if play_again == "y":
            main()
        else:
            os.system('clear')
            print("Goodbye!")
    except:
        print("Incorrect Input")
        print("Goodbye!")


def main():
    os.system('clear')

    rw = RandomWords()
    word_l = rw.random_word().lower()
    word = []
    for i in word_l:
        word.append(i)
    hangman(word, word_l)


main()
