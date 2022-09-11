# module example
print('converter module loaded....')
def getGrams(kilo):
    grams = kilo * 1000 #grams local variable 
    return grams 
def getPonds(kilo):
    ponds = kilo * 2.2
    return ponds
def getKilo(grams):
    kilo = grams/1000
    return kilo