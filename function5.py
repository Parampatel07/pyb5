#function that return multiple value 
def getResult(num1,num2):
    #local variable
    addition = num1 + num2 
    substraction = num1 - num2 
    multiplication = num1 * num2 
    division = num1 / num2 
    return addition,substraction,multiplication,division # it will return all 4 variables as tuple which will have addition as first value, substraction as second value, multiplication as 3rd value and division as 4th value 

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))

#call function 
result = getResult(num1,num2)
print(result)