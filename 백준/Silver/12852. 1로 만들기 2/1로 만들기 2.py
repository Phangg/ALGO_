import sys
from collections import deque

# bfs
def bfs(num):

    # 리스트로 데이터를 쌓을 것 => [num] 을 append
    q = deque()
    q.append([num])

    # 리스트의 최소값을 가지고 판단
    while q:
        n_lst = q.popleft()
        min_n = n_lst[0]

        if min_n == 1:
            return n_lst

        # [min_n // ?] 리스트와 n_lst 를 '+' 연산자를 통해 합쳐주기
        if min_n % 2 == 0:
            q.append([min_n//2] + n_lst)
        if min_n % 3 == 0:
            q.append([min_n//3] + n_lst)

        q.append([min_n - 1] + n_lst)

# n : 자연수
# ans : 결과 리스트
n = int(sys.stdin.readline())
ans = bfs(n)

# '*' 도 오랜만이라 그런지 기억이 안나더라..?
print(len(ans) - 1)
print(*ans[::-1])
