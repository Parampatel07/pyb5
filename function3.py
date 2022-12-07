# user defined function 
# // with argument without return value (default argument)
def PrintLine(letter='.',count=100):
    print(letter*count)
    return None

#run/call function
PrintLine(count=100)
print("Learning python")
PrintLine(count=200,letter='$')
