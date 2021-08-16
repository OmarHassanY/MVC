
#Checks if the entered movie name is a valid movie name
def ValidName(name):
    if (len(name) <= 0):
        return False

    if (name.isspace() == True):
        return False

    return True

#validates a entered movie rating category
def ValidRating(rating):
    if (rating == "PG" or rating == "G" or rating == "PG-13" or rating == "R" or rating == "NC-17" or rating=="None"):
        return True
    return False

#given the number of days of the rental calculate extra charge at 2 dollars a day over rental time
def OverdueCharge(rentalTime, actualDaysRented):
    if (actualDaysRented > rentalTime):
        return (actualDaysRented - rentalTime) * 2
    else:
        return 0


Inventory = [5,2,4,3,6,4]
#Checks if the movie of id movieID is in stock in that amount in our inventory array
def InStock(movieID, numberOfMovies):
    if (len(Inventory) < movieID ):
        print("Invalid Movie ID")
        return None
    if (Inventory[movieID] > numberOfMovies):
        return False
    else:
        return True
