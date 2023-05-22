def solution(targets):
    sort_targets_lst = sorted(targets, key = lambda x: x[0])
    
    cnt = 1
    start_point, end_point = sort_targets_lst[0]
    
    for target in sort_targets_lst[1:]:
        next_start, next_end = target[0], target[1]        
        
        if next_start < end_point:
            if next_end < end_point:
                end_point = next_end
            continue
        else:
            start_point, end_point = next_start, next_end
            cnt += 1
    
    return cnt