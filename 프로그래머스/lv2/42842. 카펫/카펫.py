# (brown // 2) + 2 => 가로 + 세로
# length, width = 가로, 세로
# (width - 2) * (length - 2) == yellow

def solution(brown, yellow):
    l_w_sum = (brown // 2) + 2
    
    answer = []
    for line in range(3, l_w_sum - 3 + 1):
        if (line - 2) * (l_w_sum - line - 2) == yellow:
            answer.append(l_w_sum - line)
            answer.append(line)
            break
    
    return answer