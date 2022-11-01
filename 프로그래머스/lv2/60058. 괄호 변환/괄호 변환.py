def make_uv(p):
    open_p = 0
    close_p = 0
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i+1], p[i+1:]

def u_is_real(u):
    stack = []
    for j in u:
        if j == '(':            
            stack.append(j)
        else:                 
            if not stack:      
                return False
            stack.pop()         
    return True

def solution(p):
    if not p:
        return ""

    u, v = make_uv(p)

    answer = ''
    if u_is_real(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for k in u[1:len(u)-1]:
            if k == '(':
                answer += ')'
            else:
                answer += '('

    return answer
