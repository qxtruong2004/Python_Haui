import Exchange as e
n = (int)(input("Nhập vào số dặm bay: "))
m = (int)(input("Nhập vào tiền / 1 dặm: "))
total = n*m
print("Tổng số tiền phải trả là: ", total, " VND")
print("Đổi sang USD: ", e.change_usd(total))
print("Đổi sang EUR: ", e.change_eur(total))
print("Đổi sang JPY: ", e.change_jpy(total))
