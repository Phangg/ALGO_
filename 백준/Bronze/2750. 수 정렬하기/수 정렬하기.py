N = int(input())

lst = [int(input()) for _ in range(N)]

lst.sort()
for j in lst:
    print(j)