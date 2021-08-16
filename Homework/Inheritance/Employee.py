import pickle
import os
class Employee():
    def __init__(self,name,id,dpt,jobTitle ):
        self.name=name
        self.id=id
        self.dpt=dpt
        self.jobTitle=jobTitle
        #self.dictionary={}
        #self.dictionary[self.name]=self
dictionary={}
doc="employees.txt"
if os.path.exists(doc):
     with open(doc,'rb') as file:
        dictionary=pickle.load(file)        
while True:
    print("Menu")
    print("-----------------------------------------")
    print("1. Look up an employee ")
    print("2. Add a new employee")
    print("3. Change an existing employee")
    print("4. Delete an employee")
    print("5. Quit the program")
    print("Enter your choice")
    choice=input()

    if choice==str(1):
        print("Enter an employee ID number:")
        id=input()
        if id in dictionary.keys():
            print("Name: "+dictionary.get(id).name)
            print("ID number: "+dictionary.get(id).id)
            print("Department: "+dictionary.get(id).dpt)
            print("Title: "+dictionary.get(id).jobTitle)
        else:
            print("That employee ID number does not exist")



    elif choice==str(2):
        print("Enter employee name: ")  
        name=input()
        if name.isnumeric()==True or not name:
                print("You have to enter  strings ")
                continue
        print("Enter employee ID number:")
        id=input()
        if id.isnumeric()==False or not id:
                print("ID numbers should only be numbers")
                continue
        if id in dictionary.keys():
            print("That employee ID number already exists")
            continue

        print("Enter employee department")
        dpt=input()
        if dpt.isnumeric()==True or not dpt:
                print("You have to enter  strings")
                continue
        print("Enter employee title")
        title=input()
        if title.isnumeric()==True or not title:
                print("You have to enter  strings")
                continue
        employee=Employee(name,id,dpt,title)
        dictionary[employee.id]=employee
        print("The new employee has been added")
        
    elif choice==str(3):
        print("Enter the employee ID number to update his info: ")
        id=input()
        if id in dictionary.keys():
            print("Enter New employee name: ")
            name=input()
            if name.isnumeric()==True or not name:
                print("You have to enter  strings")
                continue
            
            print("Enter New employee department")
            dpt=input()
            if dpt.isnumeric()==True or not dpt:
                print("You have to enter  strings")
                continue
            print("Enter New employee title")
            title=input()
            if title.isnumeric()==True or not title:
                print("You have to enter  strings")
                continue
            employee=Employee(name,id,dpt,title)
            dictionary[employee.id]=employee
            print("The employee info has been changed successfully")
        else:
            print("That employee ID number does not exist")
    
    elif choice==str(4):
        print("Enter employee ID number to delete : ")
        id=input()
        if id in dictionary.keys():
            dictionary.pop(id)
            print("Employee successfully deleted")
        else:
            print("That employee ID number does not exist")
    elif choice==str(5):
        pickle_out=open("employees.txt","wb")
        pickle.dump(dictionary,pickle_out)
        pickle_out.close()
        break
    else:
        print("Please choose options 1 or 2 or 3 or 4 or 5")
        
        

    
        
        
