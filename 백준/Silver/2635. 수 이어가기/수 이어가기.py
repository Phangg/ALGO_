import sys

N = int(sys.stdin.readline())
x = 0
ans = []
max_cnt = 0
for i in range(N//2, N+1):
    lst = []
    lst.append(N)
    lst.append(i)
    x = N - i
    cnt = 2
    n = N
    while x >= 0:
        lst.append(x)
        cnt += 1
        n = i
        i = x
        x = n - i
        if max_cnt < cnt:
            max_cnt = cnt
            ans = lst[:]
print(max_cnt)
print(*ans)
