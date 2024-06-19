from Vector.Vector_input import Vector_info
from Vector.Vecter_calc import solve

#nhập 1 vector và in ra màn hình
print("====Nhập tọa độ của vector thứ nhất===")
a = Vector_info.nhap()

print("====Nhập tọa độc của vector thứ hai=== ")
b = Vector_info.nhap()

#cộng hai vector
c = solve.cong_vector(a, b)
print(c)

# trừ 2 vector
d = solve.tru_vector(a, b)
print(d)

#tính khoảng cách OX
solve.khoangcach(d)

#tìm điểm đối xứng
solve.doixung(b)