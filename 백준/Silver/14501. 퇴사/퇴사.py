N = int(input())
T_lst = []
P_lst = []
for _ in range(N):
    T, P = map(int, input().split())
    T_lst.append(T)
    P_lst.append(P)                                                  

max_p = [0] * (N + 1)
for i in range(N-1, -1, -1):
    if T_lst[i] + i > N:
        max_p[i] = max_p[i + 1]
    else:
        max_p[i] = max(P_lst[i] + max_p[i + T_lst[i]], max_p[i + 1]) 
print(max_p[0])    