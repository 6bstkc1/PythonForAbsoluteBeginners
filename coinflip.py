import random

heads = 0
tails = 0
flips = 0

while flips < 100:
    val = random.randint(0,1)
    if val == 1:
        heads += 1
    else:
        tails += 1
    flips += 1

print("Head count: " + str(heads) + " Tail count: " + str(tails))
