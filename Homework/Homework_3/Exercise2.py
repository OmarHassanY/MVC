numbers = []
sum = 0
for i in range(10):
    print("Enter number "+ str(i+1) +" of 10: ")
    answer=input()
    numbers.append(answer)
    sum+=float(answer)
    numbers.sort(key=int)

print("Low: "+str(numbers[0]))
print("High: "+str(numbers[9]))
print("Total: "+str(format(sum,',.2f')))
print("Average: "+str(format(sum/10,',.2f')))
