# write a programe to print hollow inverted half pyramid
space=0
count=0
flash=4
while count<7:
    print("*",end="")
    count+=1
print("")
print("*",end="")
while flash>0:
    while space<flash:
        print(" ",end="")
        space+=1
    print("*",end="")
    print("")
    print("*",end="")
    space=0
    flash-=1
# print("")
# print("*")