
from math import pi

# Exercise 1 : Geometry
# Write a class called Circle that receives a radius as argument (default is 1.0)
# Write two instance methods to compute perimeter and area
# Write a method that prints the geometrical definition of a circle

class Circle():

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = 0
        self.perimeter = 0

    def set_radius(self, new_radius):
        self.radius = new_radius

    def calculate_area(self):
        self.area = (pi * self.radius)**2
        return self.area

    def calculate_perimeter(self):
        self.perimeter = 2*pi*self.radius
        return self.perimeter

    def what_is_a_circle(self):
        return '''
A circle is the set of all points in the plane that are a fixed distance (the radius)
from a fixed point (the centre). Any interval joining a point on the circle to the centre
is called a radius. By the definition of a circle, any two radius have the same length.
        '''

circle1 = Circle(10)
circle1_area = circle1.calculate_area()
circle1_perimeter = circle1.calculate_perimeter()
print(circle1.what_is_a_circle())