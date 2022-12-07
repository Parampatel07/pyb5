# write a program to findout binary number of given number using recursion 
def dectobin(number):
    if number>0:
        reminder = number%2
        number = number//2 # 5
        dectobin(number)
        print(reminder,end=' ')
    
num = int(input("Enter number to get its binary equalvent")) #5
dectobin(number=num)