a = ['python' , '123', 'java', 'c++', '19112004']
b = tuple(a)
soluong = 0
for i in range(len(b)):
    if (b[i].isdigit()):
        soluong+=1
    else: soluong += 0
print('Số lượng: ', soluong)
