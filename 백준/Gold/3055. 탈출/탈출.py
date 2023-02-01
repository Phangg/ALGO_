import sys
from collections import deque

# r : 세로 / c : 가로
# forest : 숲 2차원 리스트
# 비어있는 곳은 '.' / 물이 차있는 지역은 '*' / 돌은 'X'
# 비버의 굴은 'D' / 고슴도치의 위치는 'S'
r, c = map(int, sys.stdin.readline().split())
forest = []
for _ in range(r):
    forest.append(list(sys.stdin.readline().strip()))

# time_cnt_lst : 고슴도치의 이동시간 체크용 2차원 리스트
# q : deque
# w_lst : 물 좌표를 담을 리스트
# goal_x, goal_y : 목표(비버 굴) 좌표
# check : 도착 / 미도착 체크용 flag
time_cnt_lst = [[0 for _ in range(c)] for _ in range(r)]
q = deque()
w_lst = []
goal_x, goal_y = 0, 0
check = 1

for i in range(r):
    for j in range(c):
        if forest[i][j] == 'S':
            q.append((i, j))
        elif forest[i][j] == '*':
            w_lst.append((i, j))
        elif forest[i][j] == 'D':
            goal_x, goal_y = i, j

# 고슴도치는 물을 갈 수 없지만, 물은 고슴도치를 덮을 수 있다.
# 그래서 고슴도치 먼저 q 에 담아주는 것이 중요...!!
for wi, wj in w_lst:
    q.append((wi, wj))

while q:
    x, y = q.popleft()

    # 도착지점 ? -> flag(check) 처리 하고, break
    if x == goal_x and y == goal_y:
        check = 0
        break

    for xi, yj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nx, ny = x + xi, y + yj
        if (0 <= nx < r) and (0 <= ny < c):
            if forest[x][y] == 'S':
                if forest[nx][ny] == '.' or forest[nx][ny] == 'D':
                    forest[nx][ny] = 'S'
                    time_cnt_lst[nx][ny] = time_cnt_lst[x][y] + 1
                    q.append((nx, ny))
            elif forest[x][y] == '*':
                if forest[nx][ny] == '.' or forest[nx][ny] == 'S':
                    forest[nx][ny] = '*'
                    q.append((nx, ny))

if check:
    print('KAKTUS')
else:
    print(time_cnt_lst[goal_x][goal_y])