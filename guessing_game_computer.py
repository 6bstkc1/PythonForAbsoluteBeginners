import random

print("\tWelcome to 'Guess My Number'!\n")
print("\tI'm thinking of a number between 1-100.\n")
print("\tTry to guess it in as few attempts as possible.\n")

number = int(input("Enter a number between 1-100: "))

lower = 1
upper = 101

guess = (upper + lower) // 2
tries = 1

while guess != number and tries < 10:
    print(str(guess))
    if guess > number:
        print("Lower...")
        upper = guess
    else:
        print("Higher...")
        lower = guess
        
    guess = (upper + lower) // 2
    tries += 1

if tries == 10:
    print("The computer failed to guess the number.")
else:
    print("The computer guessed it!\n")
    print("It took this many tries " + str(tries))
    
