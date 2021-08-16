import os
if os.path.exists('charge_accounts.txt'):
    while True:
        print("Enter the account number")
        number=input()
        with open('charge_accounts.txt') as file:
            line=file.read()
            if number in line:
                print("Account number "+number+" is  valid")
            else:
               print("Account number "+number+" is  not valid") 
               

            print("Do you want to ask another question? (y or n)")
            choice=input()
            if choice =='n':
                break
else: print('File does not exist')
    
