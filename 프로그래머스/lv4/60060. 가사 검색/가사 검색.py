from bisect import bisect_left, bisect_right

def count_len(arr, l, r):
    r_idx = bisect_right(arr, r)
    l_idx = bisect_left(arr, l)
    return r_idx - l_idx


def solution(words, queries):
    lst = [[] for _ in range(10001)]
    re_lst = [[] for _ in range(10001)]
    
    answer = []
    for word in words:
        lst[len(word)].append(word)
        re_lst[len(word)].append(word[::-1])

    for i in range(10001):
        lst[i].sort()
        re_lst[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_len(lst[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_len(re_lst[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)

    return answer