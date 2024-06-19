class Product:
    def __init__(self, name, price, total):
        self.name = name
        self.price = price
        self.total = total
        self.total_price = round(self.price * self.total, 2)

    def __str__(self):
        return f"{self.name}\t\t {self.price}\t\t {self.total}\t\t{self.total_price}"
    
class Phieu:
    def __init__(self, title_phieu, maPhieu, ngayLap, maNCC, tenNCC, diachi):
        self.title_phieu = title_phieu
        self.maPhieu = maPhieu
        self.ngayLap = ngayLap
        self.maNCC = maNCC
        self.tenNCC = tenNCC
        self.diachi = diachi
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def view_phieu(self):
        print(f"{self.title_phieu}")
        print(f"Mã phiếu: {self.maPhieu}")
        print(f"Ngày lập: {self.ngayLap}")
        print(f"Mã NCC: {self.maNCC}")
        print(f"Tên NCC: {self.tenNCC}")
        print(f"Địa chỉ: {self.diachi}")
        print("Tên hàng\t Đơn giá\t Số lượng\t Thành tiền")
        for product in self.products:
            print(product)
        print(f"Cộng thành tiền:  {self.tinh_tong_tien()}")

    def tinh_tong_tien(self):
        tong_tien = sum(pr.total_price for pr in self.products)
        return tong_tien

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{self.title_phieu}\n")
            f.write(f"Mã phiếu: {self.maPhieu}\n")
            f.write(f"Ngày lập: {self.ngayLap}\n")
            f.write(f"Mã NCC: {self.maNCC}\n")
            f.write(f"Tên NCC: {self.tenNCC}\n")
            f.write(f"Địa chỉ: {self.diachi}\n")
            f.write("Tên hàng\t Đơn giá\t Số lượng\t Thành tiền\n")
            for product in self.products:
                f.write(f"{product}\n")
            f.write(f"Cộng thành tiền:  {self.tinh_tong_tien()}\n")

# Tạo danh sách sản phẩm
sanpham = [
    Product("Tivi", 30, 2),
    Product("Quạt", 1.2, 3),
    Product("Mobi", 5, 10)
]

# Tạo phiếu
letter = Phieu("PHIẾU NHẬP HÀNG", "PH001", "1/1/2007", "NCC01", "LG-Electronic", "Khu công nghiệp Như Quỳnh A")
for product in sanpham:
    letter.add_product(product)

# In thông tin của phiếu
print("THÔNG TIN CỦA PHIẾU: \n")
letter.view_phieu()

# Lưu trữ vào file bang1.txt
letter.save_to_file("Bang1.txt")
