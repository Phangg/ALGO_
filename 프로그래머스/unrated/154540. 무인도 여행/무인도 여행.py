# 직사각형
# X or 1..9(int)
# X == 바다 & int == 무인도
# 연결된 땅 -> 하나의 무인도
# int -> 식량 (1 식량 == 1 일 버티기 가능)
from collections import deque

def day_check(i, j, arr):
    q = deque()
    q.append((i, j))
    res = int(arr[i][j])
    arr[i][j] = 'X'
    while q:
        x, y = q.popleft()
        for next_x, next_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + next_x, y + next_y
            if (0 <= nx < height) and (0 <= ny < width) and (arr[nx][ny] != 'X'):
                res += int(arr[nx][ny])
                arr[nx][ny] = 'X'
                q.append((nx, ny))
    return res
    

def solution(maps):
    global height, width
    
    height, width = len(maps), len(maps[0])
    arr_maps = []
    answer = []
    
    for idx, line in enumerate(maps):
        arr_maps.append(list(line))
        
    for i in range(height):
        for j in range(width):
            if arr_maps[i][j] != 'X':
                answer.append(day_check(i, j, arr_maps))
    
    if (answer):
        return sorted(answer)
    return [-1]