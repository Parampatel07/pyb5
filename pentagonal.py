# write a program to print following series (pentagonal  number)
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176 ... 300
# 1  4  7   10  13  
number=0
print(number)
answer=number+1
print(answer)
count=4
while answer<1000:
    answer=answer+count
    count+=3
    print(answer)
