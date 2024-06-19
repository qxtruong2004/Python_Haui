diem = {
    '123' : 9.2,
    '124' : 3.7,
    '125' : 8.5,
    '126' : 5.4
}
#cho biết có bn sv điểm tk[2.5, 3.5]
# x = 0
# for k, v in diem.items():
#     if v >= 2.5 and v <= 3.5:
#         x+= 1
# print("Có tổng tất cả: ", x)

#bổ sung 1 sinh vien vào tử điển
# diem ['127'] = 9.0
# print(diem)

#xóa mọi sinh viên có điểm < 6.0
#(không thể xóa trực tiếp, ở đây sẽ phải xóa gián tiếp)
key_to_delete = [k for k, v in diem.items() if v < 6.0]
for k in key_to_delete:
    del diem[k]

print("Danh sach sinh vien sau khi xoa", diem)