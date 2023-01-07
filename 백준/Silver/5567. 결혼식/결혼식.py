import sys

# 상근이 == 1 / 상근이는 친구 + 친구의 친구를 초대 예정
# 상근이가 초대할 동기의 수는?

# n : 동기의 수 / m : 리스트 길이
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# a 와 b , b와 a는 친구임을 보여주는 graph (양방향)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# ans = 상근이가 초대할 동기의 수
# 중복 없이 set을 사용하여 일단 상근이의 친구 체크
ans = set(graph[1])

# 상근이보다 인덱스 번호 크고, 상근이 친구일때,
for i in range(n+1):
    if (i > 1) and (1 in graph[i]):
        for j in graph[i]:
            ans.add(j)

# 상근이 본인 제외
if ans:
    print(len(ans) - 1)
else:
    print(0)