day = 1
pennies = 0.01
print('Enter the number of days ')
answer = input()
print('Day      Pennies')
print('------------------------')

for i in range(int(answer)):
    print(str(day)+'        $ '+str(pennies))
    day = day +1
    pennies = pennies * 2

print('The total salary for '+str(answer)+' days is: $ '+str(pennies))
   
