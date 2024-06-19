#nhập mảng
def vecinput():
    n = (int)(input("Nhập số lượng phần tử của mảng: "))
    c = [int(input(f"Nhập phần tử thứ {i+1}= ")) for i in range(n)]
    return c

#tính tổng các phần tử trong mảng
def vecsum(a):
    sum_c = sum(a)
    return sum_c

#chèn phần tử vào mảng
def vecinsert(a):
    n = (int)(input("Nhập vào vị trí muốn chèn: "))
    m = (int)(input("Nhập vào phần tử muốn chèn: "))
    a.insert(n, m)
    print(a)

#xoa phan tu trong mang
def vecdel(a):
    b=[]
    n = (int)(input("Nhập vào phần tử muốn xóa: "))
    for i in a:
        if(i != n):
            b.append(i)
    print('mảng sau khi được xóa: ', b)

#cong 2 mang
def vecadd(a, b):
    if len(a) == len(b):
        c = [a[i] + b[i] for i in range (len(a))]
        print('Tong 2 mảng: ', c)
    else: return 0;
