sons_dads = {"Sean":"Matt","Marley":"Sean"}
cmds = ("Add","Delete","Replace","Exit","Who","Who2")

cmd = input("Enter command\n")

while cmd != cmds[3]:
    #Nonexistent command
    if cmd not in cmds:
        print("ERROR: Command Doesn't Exist.")
        
    #Add Command entered
    elif cmd == cmds[0]:
        son = input("Enter Son to add.\n")
        if son in sons_dads:
            print("ERROR: Son to add already exists!")
        else:
            dad = input("Enter Dad\n")
            sons_dads[son] = dad
            
    #Delete Command entered
    elif cmd == cmds[1]:
        son = input("Enter Son to delete.\n")
        if son not in sons_dads:
            print("ERROR: Son to delete doesn't exist!")
        else:
           del sons_dads[son]
           
    #Replace Command entered      
    elif cmd == cmds[2]:
        son = input("Enter Son to replace.\n")
        if son not in sons_dads:
            print("ERROR: Son to replace doesn't exist!")
        else:
            dad = input("Enter New Dad\n")
            sons_dads[son] = dad
    #Exit
    elif cmd == cmds[3]:
        continue
    
    #Who
    elif cmd == cmds[4]:
        son = input("Enter Son's name.\n")
        if son not in sons_dads:
            print("ERROR: Son to print doesn't exist!")
        else:
            print("The Dad of",son,"is",sons_dads.get(son))

    #Who2
    else:
        son = input("Enter Son's name.\n")
        if son not in sons_dads:
            print("ERROR: Son to print doesn't exist!")
        else:
            if sons_dads.get(son) not in sons_dads:
                print("Son has no Grandpa.")
            else:
                print("The Grandpa of",son,"is",sons_dads.get(sons_dads.get(son)))
                
            

    cmd = input("Enter command\n")
            
            
            

