class Rectangle:
    def __init__(self, l,b):
        self.__l = l
        self.__w = b
        
    # Overloading < operator
    def __lt__(self, other):
        a1 = self.__l * self.__w
        a2 = other.__l* other.__w
        return a1 < a2


r1=Rectangle(int(input("Enter length of rect1: ")),int(input("Enter breadth of rect1: ")))
r2=Rectangle(int(input("Enter length of rect2: ")),int(input("Enter breadth of rect2: ")))
if r1 < r2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 2 has smaller area")
