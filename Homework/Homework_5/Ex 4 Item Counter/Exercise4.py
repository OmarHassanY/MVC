with open('names.txt') as file:
    counter=0
    while True:
        try:
            line = file.__next__()
            counter=counter+1
        except StopIteration:
            break
print(str(counter)+' names are read')
