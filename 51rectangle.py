class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l+self.b)
    def __str__(self):
        return (f"Rectangle({self.l} x {self.b}) "
                f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}")

r1 = Rectangle(float(input("Length of rectangle 1 : ")), float(input("Breadth of rectangle 1 : ")))
print(str(r1),"\n")
r2 = Rectangle(float(input("Length of rectangle 2 : ")), float(input("Breadth of rectangle 2 : ")))
print(str(r2),"\n")

if r1.area() > r2.area():
    print("\nRectangle 1 has the larger area.")
elif r1.area() < r2.area():
    print("\nRectangle 2 has the larger area.")
else:
    print("\nBoth rectangles have equal area.")

