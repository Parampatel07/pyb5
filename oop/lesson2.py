class person:
    def walk(self):
        print("i can walk")
    def talk(self):
        print("i can talk ")
        
class developer(person):
    def code(self):
        print("i can code ")

p1 =person()
d1 = developer()

p1.walk()
p1.talk()
d1.code()
d1.walk()