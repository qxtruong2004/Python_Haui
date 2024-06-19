# Viết chương trình Python thực hiện các yêu cầu sau:
# • Tạo một lớp cơ sở NhanVien với các thuộc tính chung như ho_ten, ma_nhan_vien và 
# phương thức tinh_luong.
# • Tạo lớp con NVVP, nạp chồng phương thức tinh_luong để tính lương dựa trên số giờ làm 
# việc.
# • Tạo lớp NVSX, nạp chồng phương thức tinh_luong để tính lương dựa trên số lượng sản 
# phẩm sản xuất.
# • Nạp chồng phương thức __str__ cho các lớp con để in ra thông tin của nhân viên.
# • Nạp chồng toán tử == kiểm tra xem 2 đối tượng nhân viên có lương bằng nhau hay 
# không.
# • Tạo 2 đối tượng thuộc các lớp NVVP và NVSX. In thông tin các nhân viên và so sánh 2 
# nhân viên có lương bằng nhau h
from abc import ABC, abstractmethod

class NhanVien(ABC):
    def __init__(self, ho_ten, maNV):
        self.ho_ten = ho_ten
        self.maNV = maNV
    @abstractmethod
    def tinh_luong(self):
        pass
    def __str__(self):
        return f"Họ tên: {self.ho_ten}, Mã NV: {self.maNV}"
    #nạp chồng toán tử ==
    def __eq__(self, other):
        if isinstance(other, NhanVien):
            return self.tinh_luong() == other.tinh_luong()
        return False
    
class NVVP(NhanVien):
    def __init__(self, ho_ten, maNV, so_gio_lam, luong_theo_gio):
        super().__init__(ho_ten, maNV)
        self.so_gio_lam = so_gio_lam
        self.luong_theo_gio = luong_theo_gio
    def tinh_luong(self):
        return self.so_gio_lam * self.luong_theo_gio
    def __str__(self):
        return f"{super().__str__()}, Số giờ làm: {self.so_gio_lam}, Lương theo giờ: {self.luong_theo_gio}, Tổng lương: {self.tinh_luong()}"

class NVSX(NhanVien):
    def __init__(self, ho_ten, maNV, so_SP, don_gia_SP):
        super().__init__(ho_ten, maNV)
        self.so_SP = so_SP
        self.don_gia_SP = don_gia_SP
    def tinh_luong(self):
        return self.so_SP * self.don_gia_SP
    def __str__(self):
        return f"{super().__str__()}, Số sản phẩm: {self.so_SP}, Đơn giá sản phẩm: {self.don_gia_SP}, Tổng lương: {self.tinh_luong()}"
    
# Tạo đối tượng NVVP
nvvp = NVVP("Nguyen Van A", "NV001", 100, 1000)

# Tạo đối tượng NVSX
nvsx = NVSX("Le Thi B", "NV002", 500, 200)

# In thông tin các nhân viên
print(nvvp)
print(nvsx)

# So sánh lương của hai nhân viên
if nvvp == nvsx:
    print("Hai nhân viên có lương bằng nhau.")
else:
    print("Hai nhân viên có lương khác nhau.")
