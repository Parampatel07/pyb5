# write a programe to find zodiac sign of user
date=int(input("Enter your birth date"))
month=int(input("Enter your birth month"))

if (date>=21 and month==3) or (date<=19 and month==4):
    # print("your sign is aries")
    malesign='aries'
elif (date>=20 and month==4) or (date<=20 and month==5):
    malesign='tarus'
print(malesign)