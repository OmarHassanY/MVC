def prime():
    print("Input a number")
    num=input()
    if int(num) > 1:
       for i in range(2,int(num)):
           if (int(num) % i) == 0:
               print(num,"is not a prime number")
               break
       else:
           print(num,"is a prime number")
    else:
       print(num,"is not a prime number")
print(prime())
