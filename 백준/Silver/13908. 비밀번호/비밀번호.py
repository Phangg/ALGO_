import sys

# 중복 순열을 구현하는 라이브러리 사용
from itertools import product

# n : 비밀번호 길이 / m : 비밀번호에 들어가는 수
n, m = map(int, sys.stdin.readline().split())

# m 이 0일 경우, p_lst 는 빈 리스트가 된다.
if m:
    # p_lst : m 개의 서로 다른 숫자 (0~9)
    p_lst = list(map(int, sys.stdin.readline().split()))
else:
    p_lst = []

# all_nums : 0~9 까지 가능한 숫자를 가지는 리스트
all_nums = [x for x in range(0, 10)]

# data : 0~9까지 n자리 수로 이루어질 수 있는 중복 순열 데이터
data = product(all_nums, repeat=n)

cnt = 0
for m_data in data:
    for p_num in p_lst:
        if p_num not in m_data:
            break
    else:
        cnt += 1

print(cnt)