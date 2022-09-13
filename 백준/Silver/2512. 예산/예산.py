import sys

N = int(sys.stdin.readline())
m_lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

s = 1
e = max(m_lst)
while s <= e:
    mid = (s + e)//2
    x = 0
    for m in m_lst:
        if m > mid:
            x += mid
        else:
            x += m
    if x > M:
        e = mid - 1
    else:
        s = mid + 1
print(e)