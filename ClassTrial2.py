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
           
while True:
    print("Enter the description of article: ")
    article=input()
    print("Enter price of article:")
    price=input()
    print("Enter the quantity of article")
    quantity=input()
    purchase=Purchase(article,price,quantity)
    cart = Cart(purchase)
    # purchase.Mylist().append(article)
    # purchase.Mylist().append(price)
    # purchase.Mylist().append(quantity)
    #cart=Cart(purchase)
    print("Do you want to continue (y or n)")
    choice=input()
    if choice=='n':
        break
    elif choice=='y':
        continue
    else:
        print("You can choose only y or n")
# cart = Cart()
print("Article \t\tPrice \t\tQuantity")


#for i in cart.myList.:
     #print(i.article+"\t"+i.price+"\t"+i.quantity+"\n")
     #print(i.article.)
#print(cart.getData().index[0])
# print(cart.myList[])
# print(cart.myList[0].article)
for i in range(len(cart.myList)):
   
    print(cart.myList[i].article+"  \t\t\t"+cart.myList[i].price+"  \t\t"+cart.myList[i].quantity)




        