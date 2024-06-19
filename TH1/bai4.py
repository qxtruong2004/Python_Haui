x = (int)(input("Nhập vào số thực x: "))
n = (int)(input("Nhập vào số nguyên n: "))
if n % 2 != 0:
    print("S = 0")
else:
    S = 2016*x
    T = x
    M = 1
    for i in range(1, n) :
        T *= x
        M *= 3
        S += T/M
    print("S= ", S)