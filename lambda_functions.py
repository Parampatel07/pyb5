#example of lambda function 
#function-name = lambda input : expression
square = lambda num : num * num
qube = lambda num : square(num) * num 
area = lambda length,width: length * width
number = int(input("enter integer number"))
result = square(number)
print("result of square =",result)

number = int(input("enter integer number"))
result2 = qube(number)
print("result of qube =",result2)

length = int(input("enter length"))
width = int(input("enter width"))

result3 = area(length,width)
print("result of area =",result3)
