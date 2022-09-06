N = int(input())

res = 0
for i in range(1, N+1):
    M = list(map(int, str(i)))
    res = i + sum(M)
    if res == N:
        print(i)
        break
    if i == N:
        print(0)
