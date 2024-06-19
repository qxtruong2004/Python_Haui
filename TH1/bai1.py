#nhập số nguyên có ít hơn 5 chữ số, in ra cách đọc
n = (int)(input('Nhập số n: '))
a = n % 10
b = (n // 10) % 10
c = (n //100) % 10
d = (n // 1000) % 10
e = ( n // 10000) % 10
print(e, d, ' nghìn ', c, ' trăm ', b, ' chục ', a, ' đơn vị' )