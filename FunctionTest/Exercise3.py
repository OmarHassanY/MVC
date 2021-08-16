def payment():
    print("Enter first name: ")
    fName=input();
    print("Enter last name:")
    lName=input()
    print("Enter current salary: ")
    salary=input()
    def output(salary): 
        if int(salary)<40000:
            newSalary=int(salary)*1.05
            print("New salary for "+fName+" "+lName+":$"+str(format(newSalary, ',.2f')))
        else :
            upperSalary=2000+int(salary)+(0.02*(int(salary)-40000))
            print("New salary for "+fName+" "+lName+":$"+str(format(upperSalary, ',.2f')))
    print(output(salary))
print(payment())


