

import math


class rectangles:
    def __init__(self):
        self.lor=[]
    def addr(self,r):
        self.lor.append(r)
        
    
class UI:
    
    def get_input(self):
        n=int(input("Enter number of rectangles : "))
        for i in range(n):
            l=[]
            for j in range(3):
                lop=[]
                pass
                
            
    def show_outut(self):
        pass

class rectangle:
    def __init__(self,p1,p2,p3):
              self.p1=p1
              self.p2=p2
              self.p3=p3
    def area():
              pass
              


class point:
    def __init__(self,a,b):
        print("Came here")
        self.x=a
        self.y=b
    def distance(self,p):
        d=sqrt((self.x-p.x)**2+(self.y-p.y)**2)
        return d
 
        
    
        return l



ui= UI()
r = ui.get_input()
ui.showoutput(r)
