# Write a programe to find bmi 
class weight:
    def __init__(self,weight):
        self.weight = weight

class height:
    def __init__(self,foot,inch):
        self.foot = foot
        self.inch = inch 
    def getTotalInch(self):
        totalinch = self.foot * 12
        totalinch = totalinch + self.inch
        return totalinch
    def getMeter(self,total_inch):
        meter = total_inch / 39.37
        return meter
    
class getbmi(weight,height):
    def __init__(self,foot,inch,weight,meter):
        weight.__init__(self)
        height.__init__(self,foot,inch)
        self.weight = float(weight)
    def getbmi(self):
        bmi = self.weight / (float(meter)*float(meter))
        print("the value of bmi is ",bmi)
        
w = weight(45)
h = height(5,7)
total_inch = h.getTotalInch()
meter = h.getMeter(total_inch=total_inch)
print("meter is ",meter)
b = getbmi(5, 7, weight=45,meter=meter)
b.getbmi()