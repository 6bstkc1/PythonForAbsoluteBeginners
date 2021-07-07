"""
count.py
has the user input three numbers
the start end and increment and
prints them
"""

start = int(input("Enter a start number: "))
end = int(input("Enter an end number: "))
inc = int(input("Enter a increment number: "))

for number in range(start,end+1,inc):
    print(number)
