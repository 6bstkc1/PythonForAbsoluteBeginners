unspent_points = 30
commands = ("Add","Remove")
attributes = {"Strength": 0,"Health": 0,"Wisdom": 0,"Dexterity": 0}

while unspent_points > 0:
    print("You have", unspent_points, "unspent points.")

    cmd = input("Do you want to Add or Remove points?\n")

    if cmd not in commands:
        print("ERROR: Non-existant Command! Try Again!")
        continue
    
    attr = input("What attribute do you want to change?\n")

    if attr not in attributes:
        print("ERROR: Non-existant Attribute! Try Again!")
        continue

    if cmd == "Add":
        attributes[attr] += 1
        unspent_points -= 1
    else:
        attributes[attr] -= 1
        unspent_points += 1

print("Final character attributes", attributes)
