import sys

def bingocheck(lst):
    ans = 0
    for row in lst:
        if sum(row) == 0:
            ans += 1
            if ans == 3:
                return ans

    c_lst = list(map(list, zip(*lst)))
    for col in c_lst:
        if sum(col) == 0:
            ans += 1
            if ans == 3:
                return ans

    cross_cnt = 0
    for x in range(5):
        if lst[x][x] == 0:
            cross_cnt += 1
            if cross_cnt == 5:
                ans += 1
                if ans == 3:
                    return ans

    re_cross_cnt = 0
    for x in range(5):
        if lst[x][-x-1] == 0:
            re_cross_cnt += 1
            if re_cross_cnt == 5:
                ans += 1
                if ans == 3:
                    return ans
    else:
        return ans

num_lst = []
bingo = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
for _ in range(5):
    nums = list(map(int, sys.stdin.readline().split()))
    for n in nums:
        num_lst.append(n)
# print(num_lst)
# print(bingo)
empty_lst = [[1]*5 for _ in range(5)]

for num in num_lst:
    flag = 0
    for i in range(5):
        for j in range(5):
            if num == bingo[i][j]:
                empty_lst[i][j] = 0
                flag = 1
                break
        if flag:
            break

    if bingocheck(empty_lst) == 3:
        print(num_lst.index(num)+1)
        break