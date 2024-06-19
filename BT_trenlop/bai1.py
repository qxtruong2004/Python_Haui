from itertools import permutations
def hoanvi(a, b, c):
    nums = [a, b, c]
    perms = list(permutations(nums))
    return perms

#đếm số lượng phần tử bằng nhau liên tiếp dài nhất trong 1 đanh sách
def dem(lst):
    max_cnt = 0
    current_cnt = 0
    for i in range (1, len(lst)):
        if(lst[i] == lst[i-1]):
            current_cnt += 1
        else:
            max_cnt = max(max_cnt, current_cnt)
            current_cnt = 1
    max_cnt = max(max_cnt, current_cnt)
    return max_cnt
a, b, c = 3, 6, 7
lst = [6,5,3,2]
def check(lst):
    incr = True
    incr_ch = True
    decr = True
    decr_ch = True
    for i in range(len(lst) - 1):
        if lst[i] < lst[i+1]:
            decr = False
            decr_ch = False
        elif lst[i] > lst[i+1]:
            incr = False
            incr_ch = False
        elif lst[i] == lst[i+1]:
            incr_ch = False
            decr_ch = False

    if incr_ch:
        print("Dãy tăng tuyệt đối")
    elif incr:
        print("Dãy tăng")
    elif decr_ch:
        print("Dãy giảm tuyệt đối")
    elif decr:
        print("Dãy giảm")
    else:
        print("Dãy không tăng không giảm")



print("Các hoán vị có thể có từ 3 số a, b, c: ", hoanvi(a,b, c), sep="\n")
print("số lượng phần tử bằng nhau liên tiếp dài nhất trong danh sách: ", dem(lst))
check(lst)