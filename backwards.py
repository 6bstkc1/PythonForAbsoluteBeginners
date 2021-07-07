"""
backwards.py
has the user input a string and prints it out backwards
"""

back = input("Enter a string to be reversed: ")

rev = ""
for letter in range(-1,-len(back)-1,-1):
    rev = rev + back[letter]

print(rev)
