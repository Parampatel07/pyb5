# write a programe to find zodiac sign of user
male_date=int(input("Enter your birth date"))
male_month=int(input("Enter your birth month"))
female_date=int(input("Enter your birth date"))
female_month=int(input("Enter your birth month"))
if (male_date>21 and male_month==3) or (male_date<=19 and male_month==4):
    # print("your sign is aries")
    malesign='aries'
elif (male_date>=20 and male_month==4) or (male_date<=20 and male_month==5):
    malesign='tarus'
elif (male_date>=21 and male_month==5) or (male_date<=20 and male_month==6):
    malesign='gemini'
elif (male_date>=21 and male_month==6) or (male_date<=22 and male_month==7):
    malesign='cancer'
elif (male_date>=23 and male_month==7) or (male_date<=22 and male_month==8):
    malesign='leo'
elif (male_date>=23 and male_month==8) or (male_date<=22 and male_month==9):
    malesign='virgo'
elif (male_date>=23 and male_month==9) or (male_date<=22 and male_month==10):
    malesign='libra'
elif (male_date>=23 and male_month==10) or (male_date<=21 and male_month==11):
    malesign='scorpio'
elif (male_date>=22 and male_month==11) or (male_date<=21 and male_month==12):
    malesign='sagittarius'
elif (male_date>=22 and male_month==12) or (male_date<=19 and male_month==1):
    malesign='capricon'
elif (male_date>=20 and male_month==1) or (male_date<=18 and male_month==2):
    malesign='aquarius'
elif (male_date>=19 and male_month==2) or (male_date<=20 and male_month==3):
    malesign='pisces'
else:
    print("Invalid input")
if (female_date>21 and female_month==3) or (female_date<=19 and female_month==4):
    # print("your sign is aries")
    femalesign='aries'
elif (female_date>=20 and female_month==4) or (female_date<=20 and female_month==5):
    femalesign='tarus'
elif (female_date>=21 and female_month==5) or (female_date<=20 and female_month==6):
    femalesign='gemini'
elif (female_date>=21 and female_month==6) or (female_date<=22 and female_month==7):
    femalesign='cancer'
elif (female_date>=23 and female_month==7) or (female_date<=22 and female_month==8):
    femalesign='leo'
elif (female_date>=23 and female_month==8) or (female_date<=22 and female_month==9):
    femalesign='virgo'
elif (female_date>=23 and female_month==9) or (female_date<=22 and female_month==10):
    femalesign='libra'
elif (female_date>=23 and female_month==10) or (female_date<=21 and female_month==11):
    femalesign='scorpio'
elif (female_date>=22 and female_month==11) or (female_date<=21 and female_month==12):
    femalesign='sagittarius'
elif (female_date>=22 and female_month==12) or (female_date<=19 and female_month==1):
    femalesign='capricon'
elif (female_date>=20 and female_month==1) or (female_date<=18 and female_month==2):
    femalesign='aquarius'
elif (female_date>=19 and female_month==2) or (female_date<=20 and female_month==3):
    femalesign='pisces'
else:
    print("Invalid input")        
print(malesign)
print(femalesign)
malesign='cancer'
femalesign='aries'
if malesign=='cancer' and femalesign=='aries':
    print("you are a crictal match")
elif malesign=='aries' and femalesign=='gemini':
    print("you are a favraboule match")
elif malesign=='gemini' and femalesign=='cancer':
    print("you are a less favraboule match")