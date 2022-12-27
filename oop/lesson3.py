class cars:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def display(self):
        print("the name of car is ",self.name)
        print("the price of car is ",self.price)
        
class parts(cars):
    def __init__(self,name,price,parts,average):
        self.parts = parts
        self.average = average
        cars.__init__(self,name,price)
    def display(self):
        print("the name of car is",self.name)
        print("the price of car is ",self.price)
        print("the parts of car is ",self.parts)
        print("the average of car is ",self.average)

c1 = cars("gtr-r34","4 crore")
c1.display()        

p1 = parts("supra","2 crore", "255", "250km")
p1.display()