from cmath import pi
import math

class Circle:
    pi=math.pi
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=pi*(self.radius**2)
        return area
    def circumference(self):
        c= 2*(pi*self.radius)
        return c
    
class Square:
    def __init__(self,side):
        self.side=side
    def area(self):
        a=self.side**2
        return a
    def perimeter(self):
        p=4*(self.side)
        return p
                 
class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        a=self.width * self.length
        return a
    def perimeter(self):
        p= 2*(self.width + self.length)
        return p
    
class Sphere:
    def __init__(self,radius):
        self.radius=radius
    def surface_area(self):
        area= 4* pi*(self.radius**2) 
        return area
    def volume(self):
        v= 4/3*(pi*self.radius**3) 
        return v      
        
                
        
        