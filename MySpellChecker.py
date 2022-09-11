print("MySpellCheck loaded....")
from textblob import Word
def isSpelling(spelling):
    word = Word(spelling)
    result = word.spellcheck()
    # print(result)
    if spelling==result[0][0]:
        return True
    else:
        return False