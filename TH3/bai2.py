a = [1, 2, 4, 3, 5, 4, 3, 6, 1, 4, 2, 7, 4, 3, 4, 8, 7, 6]
k = 18
n = (int )(input("Nhập số hàng: "))
m = (int )(input("Nhập số cột: "))
if n * m > k:
    print("Không thể tạo thành ma trận ")
else:
    # lặp đoạn mã n lần mà không cần sử dụng biến để duyệt
    x = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            x[i][j] = a.pop(0)
    print(x)
