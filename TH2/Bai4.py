from Bai4.Info import nhap
from Bai4.Solve import calc
print("Nhập tọa độ điểm A:")
a = nhap.nhap_toado()
print("Nhập tọa độ điểm B:")
b = nhap.nhap_toado()
print("Nhập tọa độ điểm C:")
c = nhap.nhap_toado()

a1 = calc.kc_tam(a)
b1 = calc.kc_tam(b)
c1 = calc.kc_tam(c)
d = min(a1, b1, c1)
if( d == a1):
    print("Điểm gần tâm nhất là A")
elif( d == b1):
    print("Điểm gần tâm nhất là B")
else: 
    print("Điểm gần tâm nhất là C")
calc.dientich(a, b, c)