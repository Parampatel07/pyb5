import random
import string

letter = string.ascii_lowercase
print(letter)
answer=''
count=0
while count<10:
    answer+="".join(random.choice(letter))
    count+=1
    
print(answer)