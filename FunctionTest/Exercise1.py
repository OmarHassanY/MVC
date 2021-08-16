def distance():
    print("Enter the distance in kilometers")
    kilo=input()
    miles=int(kilo)*0.6214
    print("The conversion of "+str(kilo)+" kilometers to miles is "+str(format(miles,'.2f'))+" miles.")
   

print(distance())
