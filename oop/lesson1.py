#Creating a class 
class person:
    def __init__(self,name):
        self.name = name
    def walk(self):
        print(f"{self.name} can walk ")
    def talk(self):
        print(f"{self.name} can talk ")

name = str(input("Enter your name "))        
p1 = person(name)
p1.walk()
p1.talk()