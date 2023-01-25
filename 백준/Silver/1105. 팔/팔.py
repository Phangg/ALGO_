import sys

# l 과 r 사이 (둘 다 숫자이지만, 문자열로 각각 입력받음)
l, r = sys.stdin.readline().split()

# ans : '8' 의 개수
ans = 0

# 두 숫자의 길이가 다르다면 -> 그 숫자들 사이에 8 안들어간거 무조건 있음
if len(l) != len(r):
    print(0)

else:
    tmp = ''
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                ans += 1
        else:
            break
    print(ans)