# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	큐에서 최댓값을 삭제합니다.
# D -1	큐에서 최솟값을 삭제합니다.

import heapq
     
def solution(operations):
    
    hq = []
    for o in operations:
        x, y = o.split()
        if x == 'I':
            heapq.heappush(hq, int(y))
        elif y == '1' and len(hq):
            hq.remove(max(hq))
        elif y == '-1'and len(hq):
            hq.remove(min(hq))
    
    answer = []
    if hq:
        answer.append(max(hq))
        if hq:
            answer.append(min(hq))
    else:
         answer = [0, 0]   
    return answer