# Nhập từ bàn phím một danh sách, mỗi item là thông tin của một hàng hóa bao gồm: Mã hàng, Tên mặt hàng, Số lượng, Giá tiền.

# Hiển thị danh sách hàng hóa vừa nhập theo định dạng: Mã hàng | Tên mặt hàng | Số lượng | Giá tiền | Tổng tiền (SL * Giá).
# Tìm giá trị tổng tiền nhỏ nhất trong các mặt hàng.
# Hiển thị ra màn hình những mặt hàng có tổng tiền nhỏ nhất.
# Đếm số lượng mặt hàng trong danh sách có số lượng > 5 và tổng tiền nhỏ hơn 25
def nhap():
    danhsach = []
    so_luong = (int)(input("Nhập số lượng phần tử trong danh sách: "))
    for i in range(so_luong):
        mahang = input("Nhập mã hàng: ")
        tenhang = input("Nhập tên hàng: ")
        soluong = (int)(input("Nhập số lượng: "))
        giatien = (float)(input("Nhập giá tiền: "))
        tongtien = soluong * giatien
        danhsach.append({
            "ma_hang": mahang,
            "ten_mat_hang": tenhang,
            "so_luong": soluong,
            "gia_tien": giatien,
            "tong_tien": tongtien
        })
    return danhsach
def view(danhsach):
    print("Mã hàng\tTên mặt hàng\tSố lượng\tGiá tiền\tTổng tiền\n")
    for x in danhsach:
        print(f"{x['ma_hang']} \t {x['ten_mat_hang']}\t\t {x['so_luong']}\t\t {x['gia_tien']}\t\t{x['tong_tien']}")
def tim_gia_min(danhsach):
    min_gia = min(x['tong_tien'] for x in danhsach)
    return min_gia
def view_tien_min(danhsach, min_total):
    for x in danhsach:
        if x['tong_tien'] == min_total:
            print(f"{x['ma_hang']} \t {x['ten_mat_hang']}\t\t {x['so_luong']}\t\t {x['gia_tien']}\t\t{x['tong_tien']}")

# Đếm số lượng mặt hàng trong danh sách có số lượng > 5 và tổng tiền nhỏ hơn 25
def dem(danhsach):
    cnt = 0
    for x in danhsach:
        if(x['so_luong'] > 5 and x['tong_tien'] < 25):
            cnt += 1
    return cnt


quanly = nhap()
view(quanly)
min_tien = tim_gia_min(quanly)
print("Sản phảm có tổng giá thấp nhất là: ", min_tien)
print("*****")
view_tien_min(quanly, min_tien)
print("============")
cnt = dem(quanly)
print("số lượng mặt hàng trong danh sách có số lượng > 5 và tổng tiền nhỏ hơn 25 là: ", cnt)