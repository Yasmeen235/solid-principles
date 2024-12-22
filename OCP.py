class Shape():
    
    def area(self):
        pass

class Circle(Shape):
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def _init_(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())