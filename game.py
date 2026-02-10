import random

number = random.randint(1, 10)
guess = int(input("Guess number from 1 to 10: "))
if guess == number:
    print("You win!")
else:
    print("Try again")
