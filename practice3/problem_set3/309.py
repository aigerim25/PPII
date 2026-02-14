class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi*(radius**2)
radius = int(input())
pi = 3.14159
circle = Circle(radius)
result = circle.area()
print(f"{result:.2f}")      
