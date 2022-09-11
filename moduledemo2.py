import MySpellChecker

word = input("Enter word to check is it correct spelling or not")
isCorrect = MySpellChecker.isSpelling(word)
if isCorrect==True:
    print("it is correct spelling")
else:
    print("it is not spelling")