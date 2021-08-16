import math
def locker():
    lockers = 100
    students = 100

    lockersOpen = int(math.sqrt(lockers))
    lockersClosed = lockers - lockersOpen
    resultLockerIsOpen = {}

    for locker in range(1 , lockers + 1):
        resultLockerIsOpen[locker] = False;
        for student in range (1, students + 1):
            if locker % student == 0:
                resultLockerIsOpen[locker] = not resultLockerIsOpen[locker]
        if resultLockerIsOpen[locker]:
            print("locker", locker, "is open")

locker()
