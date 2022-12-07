#arbitary argument list 
def PrintValues(*values):
    for item in values:
        print(item,end=' ')
    print("")
PrintValues('banana','mango','apple','pinapple','kiwi')
PrintValues('banana','mango','apple','pinapple','kiwi','mango','cherry')