from textblob import Word
spelling = input("enter spelling")
word = Word(spelling)
result = word.spellcheck()
# print(result)
if spelling==result[0][0]:
    print("it is correct spelling")
else:
    print("it is not correct spelling")