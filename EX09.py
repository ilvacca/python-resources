# Exercise 9
import random

# This is a Rectangle class without random width/length generation
class Rectangle:
    
    def __init__(self, length, width):
        self.length = self.chk_dimension(length)
        self.breadth = self.chk_dimension(width)
        self.perimeter = None

    def chk_dimension(self, dimension):
        if dimension > 20:
            return 20
        elif dimension <= 1:
            return 1
        else:
            return dimension
            
    def get_breadth(self):
        return self.breadth

    def get_length(self):
        return self.length

    def perimeter(self):
        self.perimeter = 2*self.length + 2*self.breadth
        return self.perimeter

    def __str__(self):
        if self.perimeter != None:
            return "the perimeter is {0}".format(self.perimeter)
        else:
            return "You've not set the perimeter."

# This is a Rectangle class with random width/length generation
class RandRectangle:

    def __init__(self):
        self.length= self.generate_random()
        self.width= self.generate_random()

    def generate_random(self):
        return random.random()*20
    
    def perimeter(self):
        self.perimeter = 2*self.length + 2*self.width
        return self.perimeter
    
    def area (self):
        self.area = self.length*self.width
        return self.area

if __name__ == "__main__":
    rect1=RandRectangle()
    rect2=Rectangle(4,27)
