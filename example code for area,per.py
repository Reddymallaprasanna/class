'''write a code to calculate area and circumference of a circle by using class rectangle
, create a constructor and seperate functions for area and circ and delete the constructor,
import math pi value'''
from math import pi
class Circle:
    def __init__(self,r):
        self.r=r
        print("Class obj was created.....")
    def area (self):
        return pi * (self.r ** 2)
    def circ(self):
         return 2 * pi * self.r
    def __del__(self):
        print("Created cls is deleted..")
a=int(input("Enter radius:"))
c=Circle(a)
print("Area of circle is:",c.area())
print("Circumference of circle is:",c.circ())
del Circle
