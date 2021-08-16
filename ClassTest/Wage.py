class Wage:
    def __init__(self, name,hours,wage):
        self.name=name
        self.hours=int(hours)
        self.wage=int(wage)
    def PayForWeek(self):
        if self.hours<=40:
            return self.wage * self.hours
        else:
            extra=self.hours-40
            return ((self.wage*40)+(extra*1.5*self.wage))


while True:
    print("Enter person's name" )
    name=input()
    print("Enter number of hours worked" )
    hours=input()
    print("Enter hourly wage")
    wage=input()
    pay=Wage(name,hours,wage)
    print("Pay for "+name+" $%s " %+pay.PayForWeek())
    print("Do you want to enter another value?(y or n)")
    choice=input()
    if choice=='n':
        break

        