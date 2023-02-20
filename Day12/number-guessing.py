import random
answer = random.randint(0,100)

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and a 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("You have chosen death")
    attempts = 1

print(f"You have {attempts} attempt(s) left")

while attempts >= 0:

    if attempts == 0:
        print("You are out of attempts! Sorry")
        break
    guess = int(input("Guess a number: "))
    if guess == answer:
        print("Correct guess!")
        break
    elif guess > answer:
        attempts -= 1
        print("Too high, guess again.")
        print(f"You have {attempts} attempt(s) left")
    
    elif guess < answer:
        attempts -= 1
        print("Too low, guess again.")
        print(f"You have {attempts} attempt(s) left")


