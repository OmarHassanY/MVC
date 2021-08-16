#total=0
def exam():
    i=0
    total=0
    while i<5:
        print("Enter your test scores");
        percentage=input();
        if int(percentage)>=90:
            print("Your grade is A");
        elif int(percentage)<90 and int(percentage)>=80:
            print("Your grade is B");
        elif int(percentage)<80 and int(percentage)>=70:
            print("Your grade is C");
        elif int(percentage)<70 and int(percentage)>=60:
            print("Your grade is D");
        else:
            print("Your grade is F");
        i=i+1
        total=total+int(percentage)
    average=total/5
    print("")
    print("Your average score is "+str(average))          
    print("Your total is "+str(total));
    return total
#exam()


