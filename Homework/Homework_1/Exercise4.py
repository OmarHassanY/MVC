print('Are you a Vegetarian?')
vegetarian=input()
lowVegetarian = vegetarian.lower()
print('Are you vegan?')
vegan=input()
lowVegan = vegan.lower()
print('Do you prefer Gluten-Free food?')
gluten=input()
lowGluten=gluten.lower()

if lowVegetarian =='no' and lowVegan=='no' and lowGluten =='no':
    print('Joe Gourmet Burgers.')
    
elif lowVegetarian =='yes' and lowVegan =='no' and lowGluten =='yes':
    print('Main Street Pizza Company')

elif lowVegetarian =='yes' and lowVegan =='yes' and lowGluten =='yes':
    print('Corner Cafe or The Chefs Kitchen')

elif lowVegetarian =='yes' and lowVegan =='no' and lowGluten =='no':
    print('Mama Fine Italian')
        
