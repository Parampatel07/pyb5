#example of with return value without argument function 
def getPi():
    pi = 3.14 # local variable 
    return pi #this function return value of pi variable which is 3.14

#with return value with argument function 
def getSquare(number):
    square = number * number #local variable 
    return square
radius = float(input("enter radius"))
pi = getPi()
#calculate area formula pi * r * r 
square = getSquare(radius)
area = pi * square
print(area)