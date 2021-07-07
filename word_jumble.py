"""
word_jumble.py
has the user guess a word from a random list of words
first prints number of char
gives player 5 times to guess character
have player guess word
"""

import random

WORDS = ("abacus","catering","through","traveling","greatest","threating")

word = random.choice(WORDS)

print("The length of the word is",len(word))

for i in range(5):
    letter = input("Enter a letter in a word: ")
    if letter in word:
        print("yes")
    else:
        print("no")

guess = input("Guess the word: ")
if guess == word:
    print("You Win")
else:
    print("You Lose")
