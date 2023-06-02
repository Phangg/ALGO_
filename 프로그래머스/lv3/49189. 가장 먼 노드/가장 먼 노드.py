# 양방향.. 오랜만인데..?
from collections import deque

def make_tree(n, edge):
    res = [[] for _ in range(n+1)]
    for v in edge:
        res[v[0]].append(v[1])
        res[v[1]].append(v[0])
        
    for tmp in res:
        tmp.sort()
    return res

def check(n, tree):
    start = 1
    
    visited = [-1 for _ in range(n+1)]
    visited[start] = 0
    q = deque([start])
    while q:
        node = q.popleft()
        for next_node in tree[node]:
            if visited[next_node] == -1:
                visited[next_node] = 1 + visited[node]
                q.append(next_node)
                
    return visited.count(max(visited))

def solution(n, edge):
    tree = make_tree(n, edge)
    answer = check(n, tree)
    return answer