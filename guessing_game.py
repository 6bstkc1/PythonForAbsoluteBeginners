import random

print("\tWelcome to 'Guess My Number'!\n")
print("\tI'm thinking of a number between 1-100.\n")
print("\tTry to guess it in as few attempts as possible.\n")

number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

while guess != number and tries < 10:
    if guess > number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take another guess: "))
    tries += 1

if tries == 10:
    print("You failed to guess the number.")
else:
    print("You guessed it!\n")
    print("It took you this many tries " + str(tries))
    
