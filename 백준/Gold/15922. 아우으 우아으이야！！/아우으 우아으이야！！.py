import sys

# n 개의 선분
n = int(sys.stdin.readline())

# x, y = 첫 선분 (첫 기준점)
x, y = map(int, sys.stdin.readline().split())

# ans : 출력 값
ans = 0

# n-1 번 동안 nx, ny (다음 선분)이 주어짐. 
# x 우선적 오름차순 순서 
for _ in range(1, n):
    nx, ny = map(int, sys.stdin.readline().split())

    if nx > y:
        ans += abs(x - y)
        x = nx
        y = ny
    elif (nx <= y) and (y < ny):
        y = ny
else:
    ans += abs(x - y)

print(ans)