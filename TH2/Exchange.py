#Chứa hàm quy đổi từ tiền VND ra các ngoại tệ
import Rate as r
def change_usd(a):
    money = round(a / r.usd_to_vnd, 3)
    return money
def change_eur(a):
    money = round(a / r.euro_to_vnd, 3)
    return money
def change_jpy(a):
    money = round(a / r.jpy_to_vnd, 3)
    return money
