import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

# 가장 긴 친구 만큼은 크고, 다 합친 것 보다는 작을 거니까
s = max(lst)
e = sum(lst)

while s <= e:
    mid = (s + e) // 2

    # m_cnt : m 개의 덩어리 될 때까지
    # length : 녹화 가능한 길이
    m_cnt = 1
    length = 0

    for size in lst:
        if length + size <= mid:
            length += size
        else:
            length = size
            m_cnt += 1

    if m_cnt <= m:
        e = mid - 1
    else:
        s = mid + 1

print(s)