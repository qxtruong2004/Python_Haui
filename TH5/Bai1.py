#Nhập vào từ bàn phím một ma trận a(nxm) số thực và xuất ma trận vào tệp văn bản 
# theo định dạng:
# • Dòng 1: Chứa hai số nguyên n, m.
# • Các dòng tiếp theo: Chứa các dòng của ma trận
import os
import shutil
# n = (int)(input("Nhập số dòng của ma trận: "))
# m = (int)(input("Nhập số cột của ma trận: "))
# f = open('Bai1.txt', 'w')
# f.write(f'{n} {m}\n')
# for i in range (n):
#     for j in range (m):
#         f.write(input(f'Nhập b[{i}][{j}] : '))
#         f.write(' ')
#     f.write('\n')
# f.close()

#tạo 1 thư mục
folder_name = "Thư_mục_bài_1"
# os.mkdir(folder_name)
file_name= "Bai1.txt"
# shutil.move(file_name, os.path.join(folder_name, file_name))
# print("Hiển thị nội dung thư mục: \n")
# for file in os.listdir(folder_name):
#     print(file)
#đổi tên thư mục
new_folder_name = "Folder_1"
# os.rename(folder_name, new_folder_name)

# #xóa file
# os.remove(os.path.join(new_folder_name, file_name))
#xóa thư mục
os.rmdir(new_folder_name)