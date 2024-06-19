# xA, yA = input("Nhập vào tọa độ điểm A (x y): ").split()
# xA = int(xA)
# yA = int(yA)
import math as m
xA = (int)(input("Nhập vào xA: "))
yA = (int)(input("Nhập vào yA: "))
xB= (int)(input("Nhập vào xB: "))
yB = (int)(input("Nhập vào yB: "))

#khoảng cách Ecludian
D = m.sqrt((xB-xA)**2 + (yB-yA)**2)
#khoảng cách Mahaatan
M = abs(xB - xA) + abs(yB-yA)
#khoảng cách cosin
E = 1 - ((xA * xB) + (yA * yB) ) / (m.sqrt(xA**2 + yA**2) * m.sqrt(xB**2 + yB**2))
print("D= ", D)
print("M= ", M)
print("E= ", E)

