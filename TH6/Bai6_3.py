# Viết chương trình Python thực hiện các yêu cầu sau:
# • Tạo một lớp Python có tên BankAccount đại diện cho tài khoản ngân hàng, có 
# các thuộc tính: accountNumber, tên chủ tài khoản, số dư.
# • Tạo một hàm tạo với các tham số: accountNumber, name, balance.
# • Tạo một phương thức Deposit() quản lý các hành động nạp tiền.
# • Tạo một phương thức Withdrawal() quản lý các hành động rút tiền.
# • Tạo một phương thức bankFees() để áp dụng phí ngân hàng với tỷ lệ phần trăm 
# là 5% của tài khoản số dư.
# • Tạo một phương thức display() để hiển thị chi tiết tài khoản.
# • Tạo một đối tượng thuộc lớp BankAccount, sử dụng các phương thức tương 
# ứng

class BankAccount:
    def __init__(self, accountNumber, nameAcc, balanceAcc):
        self.accountNumber = accountNumber
        self.nameAcc = nameAcc
        self.balanceAcc = balanceAcc
    def Deposit(self):
        x = (float)(input("Nhập số tiền cần nạp: "))
        self.balanceAcc += x
        print(f"Số dư tài khoản: {self.balanceAcc} ")
    def Withdrawal(self):
        x = (float)(input("Nhập số tiền cần rút: "))
        if (x > self.balanceAcc):
            print("Số tiền rút vượt quá số dư")
        else:
            self.balanceAcc -= x
            print(f"Số dư tài khoản: {self.balanceAcc} ")
    def bankFees(self):
        print("Phí ngân hàng: ", self.balanceAcc* 5 / 100)
    def display(self):
        print(f"AccountNumber: {self.accountNumber}, Tên chủ tài khoản: {self.nameAcc}, Số dư: {self.balanceAcc}")

account = BankAccount("123456789", "Nguyen Van C", 1000.0)
# Hiển thị chi tiết tài khoản
account.display()

# Nạp tiền vào tài khoản
account.Deposit()

# Rút tiền từ tài khoản
account.Withdrawal()

# Áp dụng phí ngân hàng
account.bankFees()

# Hiển thị chi tiết tài khoản sau các giao dịch
account.display()

# Yêu cầu người dùng nhập thông tin tài khoản
accountNumber = input("Nhập số tài khoản: ")
name = input("Nhập tên chủ tài khoản: ")
balance = float(input("Nhập số dư ban đầu: "))

# Tạo một đối tượng thuộc lớp BankAccount với thông tin người dùng nhập vào
account = BankAccount(accountNumber, name, balance)