import random
number = random.randint(1, 100)
guess = int(input("Guess a number: "))

while guess != number:
    if guess > number:
        print("Too high!")
    else:
        print("Too low!")
    guess = int(input("Guess again: "))
print("You got it!")
