#nhập vào 1 từ điểm gồm n tt sv, mỗi item chứa ,sv, số lượng tín chỉ

dict1 = {}
n = (int)(input("Nhập số lượng sinh viên: "))
for i in range (1, n+1):
    masv = input(f"Nhập MSV cho sv {i}: ")
    so_tc = (int)(input(f"Nhập số TC của sv {i}: "))
    dict1[masv] = so_tc
print("Danh sách từ điển sinh viên: \n")
for k, v in dict1.items():
    print(k," : " ,v)

dict2 = {
    "IT6031" : "Python",
    "IT6032": "Cấu trúc dữ liệu và giải thuật",
    "IT6033" : "Thiết kế Web"
}
print("Danh sách từ điển lớp học phần:")
for k, v in dict2.items():
    print(k," : " ,v)
#kiểm tra 1 msv có trong từ điển không, nếu kh có thì bổ sung thoog tin
id = "sv02"
if id in dict1:
    print("Có mã sinh này")
else:
    print("Không tồn tại mã sinh viên này")
    soTc_new = (int)(input("Nhập số tc cho sinh viên này: "))
    dict1[id] = soTc_new
print(dict1)
#xóa các sinh viên có số tc = 0
ma_sv_xoa = [masv for masv, so_tc in dict1.items() if so_tc == 0]
for masv in ma_sv_xoa:
    dict1.pop(masv)
print(dict1)
list1 = list(dict1.keys())
list2 = list(dict1.values())
print(list1)
print(list2)
print("3 phần tử đầu tiên của list 1: ", list1[:3])
print("3 phần tử cuối của list 2: ", list2[-3:])
