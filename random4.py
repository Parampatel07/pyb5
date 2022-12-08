# Write a porgrame to create  a lucky draw on single digit number 
user_number=int(input("Enter your number "))
import random
lucky_number=random.randint(0,9)
i=True
while i==True:
    if user_number==lucky_number:
        print("cong.. you have selected correct number ")
        i=False
    else:
        print("better luck next time ")
        user_number=int(input("Enter your number "))