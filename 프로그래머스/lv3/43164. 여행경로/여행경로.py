from collections import deque

def solution(tickets):
    answer = []
    tickets.sort(key=lambda x:(x[0], x[1]))
    q = deque()
    q.append(("ICN", ["ICN"], []))
    
    while q:
        start, route, visited = q.popleft()

        if len(visited) == len(tickets):
            return route
        
        for idx, ticket in enumerate(tickets):
            if ticket[0] == start and not idx in visited:
                q.append((ticket[1], route+[ticket[1]], visited+[idx]))
                

    return 0