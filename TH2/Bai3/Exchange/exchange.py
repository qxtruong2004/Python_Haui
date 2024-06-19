#Chứa hàm quy đổi từ tiền VND ra các ngoại tệ
from Bai3.Rate import rate
def change_usd(a):
    money = round(a / rate.usd_to_vnd, 3)
    return money
def change_eur(a):
    money = round(a / rate.euro_to_vnd, 3)
    return money
def change_jpy(a):
    money = round(a / rate.jpy_to_vnd, 3)
    return money