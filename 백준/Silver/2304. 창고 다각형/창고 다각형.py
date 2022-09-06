import sys

lst = [0] * 1001
max_h = 0
max_h_idx = 0
max_w = 0

N = int(sys.stdin.readline())
for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    lst[L] = H
    if max_h < H:
        max_h = H
        max_h_idx = L
    max_w = max(max_w, L)


stack = []
ans = 0
for i in range(max_h_idx+1):
    if not stack:
        stack.append(lst[i])
        ans += stack[-1]
    else:
        if stack[-1] < lst[i]:
            stack.pop()
            stack.append(lst[i])
        ans += stack[-1]

stack = []
for i in range(max_w, max_h_idx, -1):
    if not stack:
        stack.append(lst[i])
        ans += stack[-1]
    else:
        if stack[-1] < lst[i]:
            stack.pop()
            stack.append(lst[i])
        ans += stack[-1]
print(ans)