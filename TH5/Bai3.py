# Cho bộ dữ liệu (link lấy dữ liệu tại đây, ctrl + click). Đọc toàn bộ nội dung của tệp dữ 
# liệu lên các biến n, m, a trong đó n, m là các số nguyên và a là một mảng thực.
# • In mảng đọc được ra màn hình.
# • Tính trung bình cộng từng cột dữ liệu, in kết quả ra màn hìn
from pprint import pprint
with open('Iris.txt', 'r') as file1:
    n, m = (int (x)  for x in file1.readline().split())
    a = []
    for  line in file1.readlines():
        list_str = line.split()
        a.append([float (x) for x in list_str])
print(n, m)
pprint(a)

#tính TBC từng cột
x = len(a)
y = len(a[0])
cols_sum = [sum(col) / x for col in zip(*a)]
for j, cols_sum in enumerate(cols_sum):
    print(f'Trung bình cột {j+1}: {cols_sum:.2f}')
