n = (int)(input("Nhập số lượng sinh viên: "))
danhsach = []
for i in range(1, n+1):
    a = input(f"Nhập tên sinh viên thứ {i}: ")
    danhsach.append(a)
print("Thông tin danh sách sinh viên là: ", danhsach)
#để khởi tạo 1 tuple thì ta khởi tạo 1 list rồi chuyển sang kiểu tuple
TUPLE = tuple(danhsach)
print("Thông tin của tuple là: ", TUPLE)