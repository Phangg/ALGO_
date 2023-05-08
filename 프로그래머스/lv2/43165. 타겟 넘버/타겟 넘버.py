from collections import deque

def solution(numbers, target):
    answer = 0
    res_lst = [0]
    for num in numbers:
        tmp = []
        for res in res_lst:
            tmp.append(res + num)
            tmp.append(res - num)
        res_lst = tmp

    for res in res_lst:
        if res == target:
            answer += 1
            
    return answer