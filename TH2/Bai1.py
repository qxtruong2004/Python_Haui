#viết hàm kiểm tra 1 số nguyên có phải số nguyên tố không
def snt(a):
    for i in range(2, int(a/2)+1):
        if a % i == 0:
            return False
    return True

#viết hàm kiểm tra 1 số nguyên có phải số đối xứng không
def doixung(a):
    b = 0
    c = a
    while a > 0:
        r = a % 10
        b = b * 10 + r
        a //= 10
    if b == c: return True
        # print("Số ", a, " là số đối xứng")
    return False
        # print("Số", a, " không là số đối xứng")

# nhập vào 2 số nguyên S và E, quy định S < E và E không có quá 8 chữ số, nếu sai cho nhập lại
#Tính tổng toàn bộ các số vừa nguyên tố, vừa đối xứng trong đoạn [S, E].
def tonghop():
    S = (int)(input("Nhập số nguyên S: "))
    E = (int)(input("Nhập số nguyên E: "))
    while(S > E or E > 99999999):
        print("Mời bạn nhập lại giá trị")
        S = (int)(input("Nhập số nguyên S: "))
        E = (int)(input("Nhập số nguyên E: "))
    sum =  0
    for i in range (S, E+ 1):
        if snt(i) and doixung(i):
            print(i, sep=" ")
            sum+=i
    print("Sum= ", sum)
tonghop()
# n = (int)(input("Nhập số nguyên n: "))
# if snt(n):
#     print(n, " là số nguyên tố")
# else: print(n, " không phải là số nguyên tố")
# doixung(n)
