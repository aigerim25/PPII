class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
length, width = map(int,input().split())
rec = Rectangle(length,width)
calc_area = rec.area()
print(calc_area)

