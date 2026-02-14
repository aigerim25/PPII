# def Area():
#     len = int(input())
#     return len*len
# print(Area())      
class Square():
    def __init__(self,length):
        self.length = length
    def Area(self):
        return self.length * self.length
length = int(input())
square = Square(length)
calc_area = square.Area()
print(calc_area)     

