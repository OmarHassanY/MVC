
'''
#Question 1
sales=5.9988
print(format(sales, ".2f"));

#Question 2
number=1234567.456
print(format(number, ",.1f"));

'''
#Question 3
print('Enter the speed')
speed=input()
if int(speed)<=56 and int(speed)>=24:
    print('Speed is normal')
else: print('Speed is abnormal')

'''
#Question 4
print('Enter the amount 1');
amount1=input();
print('Enter the amount 2');
amount2=input();
if int(amount1)>int(amount2):
    print('Amount 1 is greater than amount 2');
elif int(amount2)>int(amount1):
     print('Amount 2 is greater than amount 1');
else: print('The same');
    


#Question 5
print('Enter a percentage');
grade=input();
#while grade=='stop':
if int(grade)>=90:
    print('A')
elif int(grade)<90 and int(grade)>=80:
     print('B');
elif int(grade)<80 and int(grade)>=70:
    print('C');
else:print('D');


#Question 6
while True:
    print('Enter the first number');
    firstNumber=input();
    print('Enter the second number');
    secondNumber=input();
    total=int(firstNumber)+int(secondNumber)
    sumTotal=+total
    print(str(sumTotal))
    if total=='':
        break;
        

#Question 7

for x in range(0,191):
    x=x+10;
    print(x);
    
    
   
  

#Question 8
print('Enter a non zero positive number');
digit=input();
if int(digit)<=0:
    print('enter a positive non-zero number');

#Question 9
print('Enter a number in range 1 - 100');
i=input();
if int(i)<1 or int(i)>100:
    print('Number NOT int the range');
'''
    
