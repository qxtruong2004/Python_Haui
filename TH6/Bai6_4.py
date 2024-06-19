import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
class Circle:
    def __init__(self, a, b, r):
        self.center = Point(a, b)
        self.r = r
    def Area(self):
        return math.pi * self.r * self.r
    def Perimeter(self):
        return 2 * math.pi * self.r
    def testBelongs(self,x, y):
        point = Point(x , y)
        distance = math.sqrt((point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2)
        return distance

circle = Circle(0, 0, 4)
point_x, point_y = 3, 4
if (circle.testBelongs(point_x, point_y) >= 0):
    print(f"Điểm A{point_x}, {point_y} thuộc đường tròn")
else:
    print(f"Điểm A{point_x}, {point_y} không thuộc đường tròn")

    
    