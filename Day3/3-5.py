# create a program that tests the compatibility between two people
'''
take both peoples names and check for the number of times the letters in the word TRUE occurs. Then check the number of times the letters in the word LOVE occurs. 
Combine these numbers to make a 2digit number

<10 or >90, 'Your score is x, you go together like coke and mentos'
40-50, 'your score is x, you are alright together'
Otherwise, just display the score
'''


def five():

    n1 = input("Enter the name of the first person : - ").upper()
    n2 = input("Enter the name of the second person : - ").upper()

    true_score = n1.count('T')+n2.count('T')+n1.count('R')+n2.count('R') + \
        n1.count('U')+n2.count('U')+n1.count('E')+n2.count('E')
    love_score = n1.count('L')+n2.count('L')+n1.count('O')+n2.count('O') + \
        n1.count('V')+n2.count('V')+n1.count('E')+n2.count('E')

    score = str(true_score) + str(love_score)
    score = int(score)

    if score < 10 or score > 90:
        print("Your score is {}. You go together like coke and mentos".format(score))
    elif score >= 40 and score <= 50:
        print("Your score is {}. You are alright together".format(score))
    else:
        print("Your score is {}".format(score))


five()
