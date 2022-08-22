# write a programe to find bmi of user take input from user
weight=float(input('Enter your weight in kg'))
foot=int(input('Enter your height in foot'))
inch=int(input("Enter your height inch"))

meter=foot/3.281
# print(meter)

inch_meter=inch/39.37
# print(inch_meter)

height=meter+inch_meter
# print(height)

bmi=weight/(height*height)
print(bmi)

