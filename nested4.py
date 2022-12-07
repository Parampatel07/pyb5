temp=1
flash=6
while flash>0:
    count=1
    while count<flash:
        print(temp,end=" ")
        count+=1
    print("")
    temp+=1
    flash-=1