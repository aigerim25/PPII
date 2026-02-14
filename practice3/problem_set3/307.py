import math
class Point:
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1 = x1 
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3 
        self.y3 = y3
class Euclidean(Point):
    def __init__(self,x1,y1,x2,y2,x3,y3):
        super().__init__(x1,y1,x2,y2,x3,y3)
        self.diff_x = self.x3 - self.x2
        self.diff_y = self.y3 - self.y2 
    def Calc(self):
        self.dist = math.sqrt(pow(self.diff_x,2) + pow(self.diff_y,2))
        print(f"{self.dist:.2f}")
class Show(Point):
    def __init__(self,x1,y1,x2,y2,x3,y3):
        super().__init__(x1,y1,x2,y2,x3,y3)
    def reading(self):
        print(f"({self.x1}, {self.y1})")
        print(f"({self.x2}, {self.y2})")
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
obj = Show(x1,y1,x2,y2,x3,y3)
obj.reading()
e = Euclidean(x1,y1,x2,y2,x3,y3)
e.Calc()


