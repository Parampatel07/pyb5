#write a program to remove duplicate value from list using function
def getUniqueValues(*values):
    list = [] #empty list
    for item in values:
        if not item in list:
            list.append(item)
    return list 
list = getUniqueValues('banana','mango','apple','pinapple','kiwi','mango','cherry')
print(list)
