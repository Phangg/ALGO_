import sys

# n : 삼각형 길이
n = int(sys.stdin.readline())
# tri : 삼각형 (2차원 배열)
tri = []
for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

x = 2
# i -> 2번쨰 줄부터 시작
for i in range(1, n):
    # j -> 2번쨰 줄은 2개, 3번째 줄은 3개 ... 1개씩 증가
    for j in range(x):
        # 맨 처음 -> 위에 줄에서 내려오는 숫자 1가지 경우만 가능
        if j == 0:
            tri[i][j] += tri[i-1][j]
        # 맨 뒤 -> 위에 줄에서 내려오는 숫자 1가지 경우만 가능
        elif i == j:
            tri[i][j] += tri[i-1][j-1]
        # 니머지 -> max(오른쪽에서 내려온 거, 왼쪽에서 내려온 거)
        else:
            tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])
    x += 1

print(max(tri[n-1]))