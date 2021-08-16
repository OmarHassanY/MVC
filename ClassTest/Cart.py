class Purchase:
    def __init__(self, article,price,quantity):
        self.article=article
        self.price=price
        self.quantity=quantity
        #Cart(self)
        #cart.shop(self)
    # def Format(self):
    #     print("Article      Price  Quantity")
    #     print()
class Cart:    
    myList=[]
    def __init__(self,purchase):
        #self.myList =myList
        self.myList.append(purchase)
    def getData(self):
        self.myList.append(purchase)
        return self.myList
        
        # self.myList.append(purchase.price)
        # self.myList.append(purchase.quantity)

choice = 'y'        
while choice == 'y':
    print("Enter the description of article: ")
    article=input()
    if article.isnumeric()==True or not article:
        print("Please fill in properly")
        continue
    print("Enter price of article:")
    price=input()
    if price.isnumeric()==False or not price or int(price)<=0:
        print("Please fill in properly")
        continue
    print("Enter the quantity of article")
    quantity=input()
    if quantity.isnumeric()==False or not price or int(quantity)<=0:
        print("Please fill in properly")
        continue
    purchase=Purchase(article,price,quantity)
    cart = Cart(purchase)
    print("Do you want to continue (y or n)")
    choice=input()
    while choice!='y' and choice!='n':
        print("Please enter correct character (y or n)")
        choice=input()
    

print("Article \t\tPrice \t\tQuantity")


total=0
for i in range(len(cart.myList)):
   
    print(cart.myList[i].article+"  \t\t\t"+cart.myList[i].price+"  \t\t"+cart.myList[i].quantity+"\n")
    total=total+(int(cart.myList[i].price)*int(cart.myList[i].quantity))
print("Total: "+str(total))





        