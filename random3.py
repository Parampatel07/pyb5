# Write a programe to make otp 
import random

def get_otp():
    otp = str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99)) 
    print(otp) 
    
get_otp()