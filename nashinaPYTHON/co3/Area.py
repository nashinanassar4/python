from graphics.RectFunctions import* 
from graphics.CirFunctions import*
from graphics.dgraphics.SphereFunctions import*
from graphics.dgraphics.CuboidFunctions import*
l=int(input("enter length:"))
b=int(input("enter breadth:"))
print("rectangle area=",RectArea(l,b))
print("rectangle perimeter=",RectPerimeter(l,b))
r=int(input("enter radius of circle:"))
print("circle area=",CirArea(r))
print("circle perimeter=",CirPerimeter(r))
r=int(input("enter radius of sphere:"))
print("sphere area=",SpArea(r))
print("sphere volume=",SpPerimeter(r))
l=int(input("enter cuboid length:"))
b=int(input("enter cuboid breadth:"))
h=int(input("enter cuboid height:"))
print("Cuboid Area=",CubArea(l,b,h))
print("Cuboid perimeter=",CubPerimeter(l,b,h))
