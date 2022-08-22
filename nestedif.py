# write a programe to findout how to many days a month has using nested if 
month=int(input("Enter your month"))
if month<0 or month >12:
    print("invalid input")
else:
    if month==2:
        print("28 or 29 days")
    else:
        if month>7:    
            if month%2!=0:
                print("30 days")
            elif month%2==0:
                print("31 days")
        else:
            if month%2==0:
                print("30 days")
            elif month%2!=0:
                print("31 days")