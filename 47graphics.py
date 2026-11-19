import graphics.rectangle
l=float(input("Enter length of rectangle:"))
b=float(input("Enter breadth of rectangle:"))
print("Rectangle Area:", graphics.rectangle.area(l,b))
print("Rectangle Perimeter:", graphics.rectangle.perimeter(l,b))

import graphics.circle as c
r=float(input("\nEnter radius of circle:"))
print("Circle Area:", c.area(r))
print("Circle Perimeter:", c.perimeter(r))

from graphics.graphics3D.cuboid import area, perimeter
l=float(input("\nEnter length of cuboid:"))
b=float(input("Enter breadth of cuboid:"))
h=float(input("Enter height of cuboid:"))
print("Cuboid Area:", area(l,b,h))
print("Cuboid Perimeter:", perimeter(l,b,h))

from graphics.graphics3D.sphere import *
r=float(input("\nEnter radius of sphere:"))
print("Sphere Area:", area(r))
print("Sphere Perimeter:", perimeter(r))
