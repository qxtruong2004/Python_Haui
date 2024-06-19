class Item:
    def __init__(self, name, price, total):
        self.name = name
        self.price = price
        self.total = total
        self.total_price = price * total
class NCC:
    def __init__(self, id, nameNCC, address):
        self.id = id
        self.nameNCC = nameNCC
        self.address = address

class Phieu:
    def __init__(self, idPhieu, datePhieu, NCC):
         self.idPhieu = idPhieu
         self.datePhieu = datePhieu
         self.NCC = NCC
         self.items = []

    def add(self, item):
        self.items.append(item)
    def cacu(self):
        return sum(item.total for item in self.items)
    def display(self):
        print("PHIẾU NHẬP HÀNG")
        print(f"Mã phiếu: {self.idPhieu} Ngày lập: {self.datePhieu}")
        print(f"Mã NCC: {self.NCC.id} Tên NCC: {self.NCC.nameNCC}")
        print(f"Địa chỉ: {self.NCC.address}")
        print(f"{'Tên hàng':<10} {'Đơn giá':<10} {'Số lượng':<10} {'Thành tiền':<10}")
        for item in self.items:
            print(f"{item.name:<10} {item.price:<10} {item.total:<10} {item.total_price:<10}")
        total = self.cacu()
        print(f"Cộng thành tiền: {total}")

# Tạo đối tượng nhà cung cấp
ncc = NCC("NCC1", "LG-Electronic", "Khu công nghiệp Như Quỳnh A")

# Tạo đối tượng phiếu nhập hàng
phieu = Phieu("PH001", "1/1/2007", ncc)

# Thêm các mặt hàng vào phiếu nhập
phieu.add(Item("TiVi", 30, 2))
phieu.add(Item("Quạt", 1.2, 3))
phieu.add(Item("Mobi", 5, 10))

# Xuất thông tin phiếu nhập hàng
phieu.display()