# write a program to findout hexadecimal number of given number using recursion 
def dectohex(number):
    if number>0:
        reminder = number % 16
        number = number // 16
        dectohex(number)
        if reminder<=9:
            print(reminder,end=' ')
        elif reminder==10:
            print('A',end=' ')
        elif reminder==11:
            print('B',end=' ')    
        elif reminder==12:
            print('C',end=' ')    
        elif reminder==13:
            print('D',end=' ')    
        elif reminder==14:
            print('E',end=' ')    
        elif reminder==15:
            print('F',end=' ')    
            
num = int(input("Enter number to get its hexadecimal equalvent")) #5
dectohex(number=num)