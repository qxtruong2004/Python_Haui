import math as m
def khoangcach(a, b):
    x = m.sqrt((b[0] - a[0])**2 + (b[1] -a[1])**2)
    return x

def kc_tam(a):
    x = m.sqrt((a[0])**2 + (a[1])**2)
    return x
def dientich(a, b, c):
    x = khoangcach(a, b)
    y = khoangcach(b,c)
    z = khoangcach(c, a)
    if (x + y < z) or (x + z < y) or (y + z < x):
        print("Không tạo thành 1 tam giác")
    else: 
        p = (x + y + z)/ 2
        S = m.sqrt(p * (p-x) * (p-y) *(p-z))
        print('Diện tích tam giác ABC là: ', S)
