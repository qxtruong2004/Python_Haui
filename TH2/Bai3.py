from Bai3.Exchange import exchange
n = (int)(input("Nhập vào số dặm bay: "))
m = (int)(input("Nhập vào tiền / 1 dặm: "))
total = n*m
print("Tổng số tiền phải trả là: ", total, " VND")
print("Đổi sang USD: ", exchange.change_usd(total))
print("Đổi sang EUR: ", exchange.change_eur(total))
print("Đổi sang JPY: ", exchange.change_jpy(total))