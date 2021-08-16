data = {}
while True:
    print("Menu")
    print("------------------------------------------")
    print("1.Look up an email address")
    print("2.Add a new name and email address")
    print("3.Change an existing email address")
    print("4. Delete a name and email address")
    print("5.Quit the program")
    print(" ")
    print("Enter your choice: ")
    choice = input()
    if choice==str(2):
        print("Enter a new name")
        name=input()
        print("New Email:")
        email = input()
        if email in data.values():
            print(str(email)+" already in use")
        data[name]=email
    elif choice==str(1):
        print("Enter Name: ")
        name = input()
        if name in data:
            print("Name: "+name)
            print("Email: "+data.get(name))
        else:
            print(str(name)+" not in database")
    elif choice==str(4):
        print("Delete a name and email address")
        print("Write a name to delete")
        name = input()
        if name in data:
            data.pop(name)
            print("Name and email removed")
        else:
            print(str(name)+" not in database")
    elif choice==str(5):
        break
    elif choice==str(3):
        print("Update an email")
        print("Enter the name of the person")
        name = input()
        print("Enter the new email:")
        email = input()
        if name in data:
            data2 ={name:email}
            data.update(data2)
        else:
             print(str(name)+" not in database")
    else:
        print("The choice you entered is invalid.Please enter a valid choice:")
        continue

    

