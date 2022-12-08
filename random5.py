# Write a porgrame to select luck card from the given list 
import random
cards = ['spade','heart','clubs','diamonds'];
user_card=str(input("Select your card "))
i=True
lucky_card=0
while i==True:
    if user_card==lucky_card:
        print("cong...")
        i=False
    else:
        print("better luck next time ")
        print("lucky card was ",lucky_card)
        user_card=str(input("Select your card "))
        lucky_card=random.choice(cards)