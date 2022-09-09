import sys

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

lst.sort(key=lambda x: (x[0], x[1]))

for ans in lst:
    print(*ans)