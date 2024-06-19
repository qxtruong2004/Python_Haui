n = (int)(input("Nhập số nguyên n có 6 chữ số: "))
b = 0
c=n
while ( n > 0):
    r = n % 10
    b = b * 10 + r
    n//=10
if(b == c): print("Số đối xứng")
else: print('Số không đối xứng')
