import sys
from collections import deque

# t: 테스트케이스 수
t = int(sys.stdin.readline())

for _ in range(t):

    # n: 팀 수 / last_year: 작년 등수 (1~n)
    n = int(sys.stdin.readline())
    last_year = list(map(int, sys.stdin.readline().split()))

    graph = [[] for _ in range(n+1)]
    de = [0 for _ in range(n+1)]
    q = deque()
    ans = []
    flag = 0

    for i in range(n-1):
        for j in range(i+1, n):
            graph[last_year[i]].append(last_year[j])
            de[last_year[j]] += 1

    # m: 올해 순위 변동 수 / a, b: a순위 <-> b순위 변동
    m = int(sys.stdin.readline())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        flag = 1

        for i in graph[a]:
            if i == b:
                graph[a].remove(b)
                de[b] -= 1
                graph[b].append(a)
                de[a] += 1
                flag = 0

        if flag:
            graph[b].remove(a)
            de[a] -= 1
            graph[a].append(b)
            de[b] += 1

    for x in range(1, n+1):
        if de[x] == 0:
            q.append(x)

    if not q:
        print('IMPOSSIBLE')
        continue

    res = 1
    while q:
        if len(q) > 1:
            res = 0
            break

        tmp = q.popleft()
        ans.append(tmp)

        for i in graph[tmp]:
            de[i] -= 1
            if de[i] == 0:
                q.append(i)
            elif de[i] < 0:
                res = 0
                break

    if not res or len(ans) < n:
        print('IMPOSSIBLE')
    else:
        print(*ans)