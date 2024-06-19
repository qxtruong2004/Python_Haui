class Team:
    def __init__(self, code, country, federation, appearances, best_result):
        self.code = code
        self.country = country
        self.federation = federation
        self.appearances = appearances
        self.best_result = best_result

    def __str__(self):
        return f"{self.code}\t{self.country}\t{self.federation}\t{self.appearances}\t{self.best_result}"

class Tournament:
    def __init__(self, name, group, start_date, organizer, host_country, num_teams):
        self.name = name
        self.group = group
        self.start_date = start_date
        self.organizer = organizer
        self.host_country = host_country
        self.num_teams = num_teams
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def change_host_country(self, new_host):
        self.host_country = new_host

    def print_teams(self):
        print("Mã\tQuốc gia\tLiên đoàn\tSố lần tham dự\tThành tích tốt nhất")
        for team in self.teams:
            print(team)

    def find_champion_team(self):
        champions = [team for team in self.teams if "Vô địch" in team.best_result]
        if champions:
            print("Các đội từng vô địch World Cup:")
            for team in champions:
                print(team)
        else:
            print("Không có đội nào từng vô địch World Cup.")

    def sort_teams_by_appearances(self):
        self.teams.sort(key=lambda x: x.appearances, reverse=True)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Giải đấu: {self.name}\n")
            file.write(f"BẢNG: {self.group}\n")
            file.write(f"Ngày khai mạc: {self.start_date}\n")
            file.write(f"Tổ chức: {self.organizer}\n")
            file.write(f"Chủ nhà: {self.host_country}\n")
            file.write(f"Số lượng đội: {self.num_teams}\n")
            file.write("Mã\tQuốc gia\tLiên đoàn\tSố lần tham dự\tThành tích tốt nhất\n")
            for team in self.teams:
                file.write(f"{team}\n")

# Nhập thông tin bảng đấu và các đội bóng
tournament = Tournament("FIFA World Cup 2022", "B", "20/11/2022", "FIFA", "Pháp", 4)

teams = [
    Team("ENG", "Anh", "UEFA", 16, "Vô địch"),
    Team("IRN", "Iran", "AFC", 6, "Vòng bảng"),
    Team("USA", "Mỹ", "CONCACAF", 11, "Hạng ba"),
    Team("WAL", "Wales", "UEFA", 2, "Tứ kết")
]

for team in teams:
    tournament.add_team(team)

# In thông tin bảng đấu và các đội bóng
print("Thông tin bảng đấu trước khi sửa:")
tournament.print_teams()

# Sửa lại thông tin nước chủ nhà
tournament.change_host_country("Qatar")

# Kiểm tra và in thông tin đội bóng từng vô địch
tournament.find_champion_team()

# Sắp xếp các đội bóng theo số lần tham dự giảm dần và in ra màn hình
tournament.sort_teams_by_appearances()
print("\nDanh sách các đội bóng sau khi sắp xếp theo số lần tham dự:")
tournament.print_teams()

# Ghi dữ liệu bảng đấu vào file
tournament.save_to_file("BANG_B.txt")
print("\nDữ liệu đã được ghi vào file BANG_B.txt")
