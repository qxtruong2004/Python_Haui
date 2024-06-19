'''Chứa các hàm thực hiện: Nhập ba tọa độ của một véc tơ từ bàn 
phím; hiển thị véc tơ ra màn hình dạng X(x1, x2, x3).'''

def nhap():
    x1, x2, x3 = input("Nhập 3 tọa độ của 1 vector: ").split()
    x1 = float(x1)
    x2 = float(x2)
    x3 = float(x3)
    return [x1, x2, x3] #trả về 1 list

def view(vector):
    # print('Tọa độ của vector đó là: X{}, {}, {}'.format(vector[0], vector[1], vector[2]))
    print("Tọa độ: ", vector)
