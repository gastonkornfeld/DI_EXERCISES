import math

# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circlecan be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
# Other abilities of a Circle instance: * Compute the circle’s area 
# * Print the circle and get something nice * Be able to add two circles together 
# * Be able to compare two circles to see which is bigger *
#  Be able to compare to see if there are equal * Be able to put them in a list and sort them
def swap_position(list1, pos1, pos2):

    first_elem = list1.pop(pos1)
    secon_elem = list1.pop(pos2-1)
    list1.insert(pos1, secon_elem)
    list1.insert(pos2, first_elem)
    return list1


class Circle():
    list_of_circles = []
    
    
    def __init__(self, radius):
        self.radius = radius
        self. diameter = radius *2
        Circle.list_of_circles.append(self)
        
        
    def getArea(self):
        self.area = math.pi * self.radius**2
        return self.area
    
    def __repr__(self):
        return(f"circle O with radius {self.radius}")

    

    def __add__(self, other):
        area1 = self.getArea()
        area2 = other.getArea()
        total_area = area1 + area2
        new_radius = math.sqrt(total_area/math.pi)
        return f' circle 1 area = {area1} + circle 2 area {area2}, total area {total_area}, new circle radius {new_radius}'

    def isBigger(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def isEqual(self, other):
        if self.radius == other.radius:
            return True


def sortedCircles(lista):        
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j].isBigger(lista[j+1]):
                swap_position(lista, j, j+1)
    return lista



circle1 = Circle(3)
circle2 = Circle(4)
circle1 = Circle(8)
circle2 = Circle(1)
circle1 = Circle(23)
circle2 = Circle(2)
print(circle1+circle2)
print(Circle.list_of_circles)

print(sortedCircles(Circle.list_of_circles))

