S = input("Nhập xâu S: ")
Q = " java python php"
if( S in Q):
    print("S là con của Q")
else:
    print('S không phải là con của Q')
P = S + Q
print("Xâu sau khi ghép: ", P)

#thay the "c++" trong P nếu có thành Ruby
# if "c++" in P:
#     P_new = P.replace("c++", "ruby")
# print("Xâu sau khi thay the: ", P_new)

#tach xau P thanh dict vs key là số và value là xâu
words = P.split()

word_dict = {i : words[i] for i in range(len(words))}
print("Từ điển các từ: ", word_dict)