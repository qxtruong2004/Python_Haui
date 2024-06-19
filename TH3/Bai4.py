import random
a = []
for i in range (5):
    phan_tu = random.randint(0, 10)
    a.append(phan_tu)
b = []
for i  in range(5):
    phan_tu = random.randint(0, 15)
    b.append(phan_tu)
a.sort()
b.sort()
c = a+b
c.sort()
print(c)
