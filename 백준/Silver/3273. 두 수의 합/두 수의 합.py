import sys

# n : 수열의 크기
# lst : 수열 리스트
# x : 목표 숫자
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

# 이진 탐색을 위한 설정
lst.sort()
s, e = 0, n - 1
ans = 0

# tmp : 이분 탐색하면서 나오는 값
while s < e:
    tmp = lst[s] + lst[e]
    if x > tmp:
        s += 1
    elif x == tmp:
        ans += 1
        e -= 1
    else:
        e -= 1
print(ans)