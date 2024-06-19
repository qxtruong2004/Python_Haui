def nhapdict():
    n = (int)(input("Nhập số lượng học sinh: "))
    dict1 = {}
    for i in range(1, n+1):
        maSV = input(f"Nhập mã sinh viên thứ {i}: ")
        soTC = (int)(input(f"Nhập số tín chỉ của sv thứ {i}: "))
        dict1[maSV] = soTC
    return dict1
tu_dien = nhapdict()
danhsach1 = (list)(tu_dien.keys())
danhsach2 = (list)(tu_dien.values())
print("Danh sách keys: ", danhsach1)
print("Danh sách values: ", danhsach2)
