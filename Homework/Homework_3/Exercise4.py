print("Enter an integer greater than 1: ")
answer=input()
numbers = []
def prime(param):
    values = []
    for i in range(1,param+1):
        if(param%i ==0):
            values.append(i)
    return values         
for i in range(2,int(answer)+1):
    numbers.append(i)
    
    primeOrComposite=prime(numbers[i-2])
    if(len(primeOrComposite)==2):
        print(str(numbers[i-2])+" is prime")
    else:
        print(str(numbers[i-2])+" is composite")


