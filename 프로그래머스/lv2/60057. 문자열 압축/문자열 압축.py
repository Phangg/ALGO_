def solution(s):
    len_s = len(s)
    results = []

    for i in range(1, len_s + 1):
        res = ""
        cnt = 1
        tmp = s[:i]

        for j in range(i, len_s + i, i):
            
            if tmp == s[j:i + j]:
                cnt += 1
            else:
                if cnt != 1:
                    res += str(cnt)
                
                res += tmp    
                tmp = s[j:i + j]
                cnt = 1
                
        results.append(len(res))
    
    return min(results)