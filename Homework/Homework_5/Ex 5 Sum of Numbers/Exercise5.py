with open('numbers.txt') as file:
    sum=0
    while True:
        try:
            line = int(file.__next__())
            sum=sum+line
        except StopIteration:
            break
print('Total: '+str(sum))