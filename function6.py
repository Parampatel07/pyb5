#write a program to findout minimum and maximum value from given list using function 
def getMinMax(numbers):
    min = max = numbers[0] #chain assignment 
    position=1
    size = len(numbers)
    while position<size:
        if numbers[position]<min:
            min = numbers[position]
        elif numbers[position]>max:
            max = numbers[position]
        position=position+1 #2
    return min,max #function return multiple value as tuple 
numbers = [55,10,-45,-100,200,65,11,1125,500,111] #unsorted list
result = getMinMax(numbers)
print(result)
print("minimum value ",result[0])
print("maximum value ",result[1])