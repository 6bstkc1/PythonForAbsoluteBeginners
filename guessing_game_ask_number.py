import random

def ask_number(question,low,high,step=1):
    response = None
    while response not in range(low,high,step):
        response = int(input(question))
    return response

def main():
    print("\tWelcome to 'Guess My Number'!\n")
    print("\tI'm thinking of a number between 1-100.\n")
    print("\tTry to guess it in as few attempts as possible.\n")

    number = random.randint(1,100)
    guess = ask_number("Enter number between 1 and 100\n",0,100)
    tries = 1

    while guess != number and tries < 10:
        if guess > number:
            print("Lower...")
        else:
            print("Higher...")
        guess = ask_number("Enter number between 1 and 100\n",0,100)
        tries += 1

    if tries == 10:
        print("You failed to guess the number.")
    else:
        print("You guessed it!\n")
        print("It took you this many tries " + str(tries))

main()



    
