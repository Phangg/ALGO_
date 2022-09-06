import sys

# i : 인덱스 , N : 전체 인원 , n : 한팀 인원 , a : a팀, b: b팀
def team(i, N, n, a, b):
    global lst
    if i == n:
        # print(a,b)
        sum_a = 0
        sum_b = 0
        for x in range(n):
            for y in range(x, n):
                nx = a[x]
                ny = a[y]
                sum_a += S[nx][ny] + S[ny][nx]
        for x in range(n):
            for y in range(x, n):
                nx = b[x]
                ny = b[y]
                sum_b += S[nx][ny] + S[ny][nx]
        # print(sum_a, sum_b)
        gap = abs(sum_a - sum_b)
        lst.append(gap)
        return

    x = 0
    if a:
        x = max(a) + 1

    for j in range(x, N):
        if j not in a:
            a.append(j)
            if a[0] != 0:
                break
            if len(a) == n:
                for k in range(N):
                    if k not in a and k not in b:
                        b.append(k)
            team(i+1, N, n, a, b)
            a.pop()
            b.clear()

# N : 모인 인원 (짝수)
N = int(sys.stdin.readline())
# 한팀은 N/2 명
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(S)

lst = []
a = []
b = []
team(0, N, N//2, a, b)
# print(lst)

print(min(lst))