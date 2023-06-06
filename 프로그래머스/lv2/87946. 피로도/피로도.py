# [ 최소 필요 피로도 , 소모 피로도 ]
from itertools import permutations

def solution(k, dungeons):
    answer = []
    P = list(permutations(dungeons, len(dungeons)))
    for p_lst in P:
        res = 0
        tmp_k = k
        for p in p_lst:
            if p[0] <= tmp_k:
                res += 1
                tmp_k -= p[1]
        answer.append(res)
    
    if answer:
        return max(answer)
    return -1
