import myconverter

kilo = int(input("Enter kilograms "))
grams = myconverter.getGrams(kilo)
print("Grams = ",grams)
pounds = myconverter.getPonds(kilo)
print("pounds = ",pounds)

grams = int(input("Enter grams "))
kilo = myconverter.getKilo(grams)
print("kilo = ",kilo)
