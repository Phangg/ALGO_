import sys
from collections import deque

def bfs():
    # 0, 0 좌표부터 체크 (무조건 공간에서 시작)
    # cnt : 가장자리에 녹는 치즈들 카운트
    que = deque()
    que.append((0, 0))
    visited[0][0] = 1
    cnt = 0

    while que:
        x, y = que.popleft()
        for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + i, y + j
            if (0 <= nx < p) and (0 <= ny < q) and (visited[nx][ny] == 0):

                # 공간에 있다가 치즈로 이동 했을 경우? -> 가장자리
                if cheese[nx][ny]:
                    cheese[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1

                # 공간에서 공간으로 이동 -> que append
                else:
                    visited[nx][ny] = 1
                    que.append((nx, ny))

    ans.append(cnt)
    return cnt


# p : 세로 / q : 가로
# cheese : 치즈 2차원 배열
# total_cheese : 총 치즈 개수
p, q = map(int, sys.stdin.readline().split())
cheese = []
total_cheese = 0
for _ in range(p):
    lst = list(map(int, sys.stdin.readline().split()))
    total_cheese += lst.count(1)
    cheese.append(lst)

# ans : 시간마다 녹인 치즈 수 - 저장 리스트
ans = []

# hour : 시간 카운트
hour = 0

# 녹은 치즈 개수
cheese_cnt = 0

# 1시간이 지날때 마다 계속 진행
# 녹인 치즈가 총 치즈 개수와 같아지면 종료
while cheese_cnt != total_cheese:
    hour += 1
    visited = [[0 for _ in range(q)] for _ in range(p)]
    cheese_cnt += bfs()

print(hour)
print(ans[-1])