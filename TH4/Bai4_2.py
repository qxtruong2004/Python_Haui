#A chứa các mã sinh vien đăng kí học tiếng anh
a = {'123', '124', '125'}
#B chứa các mã sinh viên đăng kí học tiếng hàn
b = {'124', '126', '127'}

#cho biết có sinh vien nào học ở cả 2 bàn không
# c = a & b
# if(a&b):
#     print("Có mã sinh vien", c)
# else:
#     print("Không có")

#cho biết tổng hợp của 2 sinh viên
# d = a | b
# print("Danh sách tổng hợp: ", d)

#cho biết ds học anh không học hàn
c = a-b
print('Danh sach: ', c)