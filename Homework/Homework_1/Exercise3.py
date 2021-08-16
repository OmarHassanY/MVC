print('How many people are attending the cookout?')
numOfPeople=input()
print('How many hot dogs does each person get?')
eachHotDogs=input()
totalHotDogs=int(numOfPeople)*int(eachHotDogs)
remainderHotDogs=totalHotDogs % 10
remainderBuns=totalHotDogs % 8

if remainderHotDogs == 0:
    print('The minimum number of packages of hot dogs required is '+str(totalHotDogs))
    print('The number of hot dogs that will be left over is 0' )
    
else:
    print('The minimum number of packages of hot dogs required is '+
          str(totalHotDogs+10-remainderHotDogs))
    print('The number of hot dogs that will be left over is '+ str(remainderHotDogs))

if remainderBuns==0:
    print('The minimum number of packages of hot dog buns required is '+str(totalHotDogs))
    print('The number of hot dog buns that will be left over is 0' )
else:
    print('The minimum number of packages of hot dog buns required is '+
          str(totalHotDogs+8-remainderBuns))
    print('The number of hot dog buns that will be left over is '+ str(remainderBuns))
    
  


