from abc import ABC, abstractmethod
class Polygon(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def area(self):
        self.length=float(input("Enter length of rectangle: "))
        self.breadth=float(input("Enter breadth of rectangle: "))
        print("Area :",self.length*self.breadth)

class Triangle(Polygon):
    def area(self):
        self.base=float(input("Enter base of triangle: "))
        self.height=float(input("Enter height of triangle: "))
        print("Area :",0.5*self.base*self.height)


rect = Rectangle()
rect.area()

tri = Triangle()
tri.area()
