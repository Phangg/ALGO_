dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    d = 0
    x, y = 0, 0
    for s in range(1, N*N+1):
        arr[x][y] = s
        x += dx[d]
        y += dy[d]
        if (y >= N) or (x >= N) or (y < 0) or (x < 0) or arr[x][y]:
            x -= dx[d]
            y -= dy[d]

            d = (d + 1) % 4
            x += dx[d]
            y += dy[d]
    print(f'#{tc}')
    for ans in arr:
        print(*ans)