import sys

N = int(sys.stdin.readline())
lst = [list(sys.stdin.readline().split()) for _ in range(N)]

lst.sort(key=lambda x: int(x[0]))

for ans in lst:
    print(*ans)