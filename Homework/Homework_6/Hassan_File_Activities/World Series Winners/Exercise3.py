yearAndTeam = {}
teamAndTimes = {}
year=1903
yearList =[]
teamList=[]

with open("WorldSeriesWinners.txt") as f:
    line = f.readlines()
noOflines = sum(1 for line in open('WorldSeriesWinners.txt')) 
for i in range(noOflines+2):
    if (year+i)==1904:
        continue
    if (year+i)==1994:
        continue
    yearList.append(year+i)
for i in range(noOflines):
    teamList.append(line.__getitem__(i).strip())

#d = {List1[n]: List2[n] for n in range(len(List1))}
yearAndTeam  = {yearList[n]: teamList[n] for n in range(len(yearList))}
for v in yearAndTeam.values():
   if not v in teamAndTimes: teamAndTimes[v]=1
   else: teamAndTimes[v]+=1
while True:
    print('Enter a year in the range 1903-2009: ')
    answer=input()
    #if(int(answer)==1994 or int(answer)==1904):
    if int(answer) not in yearAndTeam.keys():
        print("The world series wasn't played in the year "+answer)
    else:
        print('The team that won the world series in '+answer+' is the '+yearAndTeam.get(int(answer)))
        print('They won the world series '+str(teamAndTimes.get(yearAndTeam.get(int(answer))))+' times')
    print('Do you want to enter another year?(y or n)')
    choice=input()
    if choice=='n':
        break
    
        