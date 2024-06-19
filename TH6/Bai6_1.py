# Xây dựng một lớp Hình chữ nhật bằng ngôn ngữ Python với các thuộc tính 
# chiều dài và chiều rộng.
# • Tạo một phương thức Perimeter() để tính chu vi của hình chữ nhật và một 
# phương thức Area() để tính diện tích của hình chữ nhật.
# • Tạo một phương thức display() hiển thị chiều dài, chiều rộng, chu vi và diện 
# tích của một đối tượng được tạo bằng cách sử dụng khởi tạo trên lớp hình chữ 
# nhật

class HCN:
    def __init__(self, cd, cr):
        self.cd = cd
        self.cr = cr 
    def Perimeter(self):
        return (self.cd + self.cr) * 2
    
    def Area(self):
        return self.cr * self.cd
    
    def display(self):
        print("Chiều dài: ", self.cd)
        print("Chiều rộng: ", self.cr)
        print("Chu vi: ", self.Perimeter())
        print("Diện tích: ", self.Area())

hinhchunhat = HCN(5, 3)
hinhchunhat.display();