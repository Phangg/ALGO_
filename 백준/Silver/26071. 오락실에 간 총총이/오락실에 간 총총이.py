import sys

# n * n 의 2차원 배열 lst
# max_i, max_j, min_i, min_j : 가장 크고 작은 가로 세로 지점
# 입력 받으면서 최소, 최대 값 구해주기
n = int(sys.stdin.readline())
max_i, max_j = 0, 0
min_i, min_j = float('inf'), float('inf')
lst = []
for i in range(n):
    tmp_lst = list(sys.stdin.readline().strip())
    for j in range(n):
        if tmp_lst[j] == 'G':
            max_i = max(max_i, i)
            max_j = max(max_j, j)
            min_i = min(min_i, i)
            min_j = min(min_j, j)
    lst.append(tmp_lst)

# ans : 최종 출력 값
ans = 0

# gom 이 1개 일 경우 어차피 0 으로 나올 것
# 가로 or 세로가 최소 최대가 같다는 건 한줄에 있다는 뜻
# i 가 같으면 j 만 확인 / j 가 같으면 i 만 확인하면 된다.

if min_i != max_i:
    ans += min(max_i, (n - 1 - min_i))

if min_j != max_j:
    ans += min(max_j, (n - 1 - min_j))

print(ans)