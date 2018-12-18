class shapes():
    def quadArea(self):
        return self.side1*self.side2
    def quadPerimeter(self):
        return self.side1*2+self.side2*2

class rectangle(shapes):
    def __init__(self,side1,side2):
        self.side1=side1
        self.side2=side2

class square(shapes):
    def __init__(self,side):
        self.side1=side
        self.side2=side

class circle(shapes):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2

class ellipse(shapes):
    def __init__(self,axisA,axisB):
        self.axisA=axisA
        self.axisB=axisB
    def area(self):
        return 3.14*self.axisA*self.axisB

rekt1=rectangle(4,5)
print(rekt1.quadArea())
print(rekt1.quadPerimeter())

sq1=square(8)
print(sq1.quadArea())
print(sq1.quadPerimeter())

circle1=circle(3.5)
print(circle1.area())

oval1=ellipse(2,4)
print(oval1.area())
