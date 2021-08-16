bday={}
while True:
    print("Friends and Their Birthdays")
    print("-------------------------")
    print("1. Look up a birthday")
    print("2. Add a new birthday")
    print("3. Change a birthday")
    print("4. Delete a birthday")
    print("5. Quit the program")
    print("Enter your choice")
    answer=input()
    if int(answer)==1:
        print("Enter a name")
        name = input()
        if name in bday:
            print(bday.get(name))
        else:
            print(str(name)+ " not in database")
    if int(answer)==5:
        break
    if int(answer)==2:
        print("Enter a name")
        name = input()
        print("Enter a birthday")
        date = input()
        bday[name]=date
    if int(answer)==3:
        print("Enter a name")
        name = input()
        if name in bday:
            print("Enter the birthday ")
            date = input()
            bday2 = {name:date}
            bday.update(bday2)
        else:
            print(str(name)+ " not in database")
        
    if int(answer)==4:
        print("Enter name of birthday to Delete")
        name = input()
        if name in bday:
            bday.pop(name)
            print("Birthday deleted")
        else:
            print(str(name)+ " not in database")
        


        

        
