days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
sales = []
totalSales=0
for i in range(len(days)):
    print("Enter the sales for "+str(days[i]))
    sales=input();
    totalSales+=float(sales)
print("Total sales for the week:$"+str(format(totalSales,',.2f')))
    
