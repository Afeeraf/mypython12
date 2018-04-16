import math
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,p):
        return math.sqrt((p.x - self.x) **2 + (p.y - self.y) ** 2)


def myinput():
    x1=float(input("x1"))
    y1=float(input("y1"))
    return point(x1,y1)



p1=myinput()
p2=myinput()
print(p1.distance(p2))
