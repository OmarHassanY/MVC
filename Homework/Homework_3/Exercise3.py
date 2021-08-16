print("Enter number to compare with list")
firstNumber=input()
numbers = []
largerNumbers = []
for i in range(4):
    print("Enter number "+str(i+1)+" of 4")
    answer=input()
    numbers.append(answer)
print("Comparison number: "+str(format(int(firstNumber),',.2f')))
print("List of numbers:")
print('[%s]' % ', '.join(map(str, numbers)))
print("List of numbers that are larger than "+str(firstNumber))
for index in range(len(numbers)-1):
    if int(numbers[index])>int(firstNumber):
        largerNumbers.append(numbers[index])
print('[%s]' % ', '.join(map(str, largerNumbers)))

