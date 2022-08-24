# write a programe to findout largest triangle out of given 3 triagnle
height1=int(input("Enter height 1 "))
base1=int(input("Enter base 1 "))
height2=int(input("Enter hieght 2"))
base2=int(input("Enter base 2"))
height3=int(input("Enter hieght 3"))
base3=int(input("Enter base 3"))
triangle1=height1*base1/2
triangle2=height2*base2/2
triangle3=height3*base3/2
if triangle3>triangle2:
    print('triagnle 3 is greater')
elif triangle2>triangle3:
    print('triangle 2 is greater')
elif triangle3>triangle1:
    print('triangle 3 is gretaer')
elif triangle3<triangle1:
    print('triangle 3 is greater')
# elif triangle1<triangle3:
#     print('triagnel 3 is greaterr')
elif triangle2>triangle1:
    print("triagnle 2 is greater")
else:
    print('triagnle 3 is gretaer')