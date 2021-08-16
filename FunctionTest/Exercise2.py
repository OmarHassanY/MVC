def fitness():
    print("Enter the fat grams consumed: ")
    fat=input()
    print("Enter the carbohydrates grams consumed")
    carbon=input()
    caloriesOfFat=int(fat)*9
    caloriesOfCarbon=int(carbon)*4
    print("Grams of fat: "+str(fat))
    print("Fat calories "+str(caloriesOfFat))
    print("Grams of carbs "+str(carbon))
    print("Carb calories "+str(caloriesOfCarbon))
print(fitness())
    
