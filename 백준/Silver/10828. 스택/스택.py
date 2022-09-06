import sys
N = int(sys.stdin.readline())
stack = []                                      # stack 과 top 설정
top = -1

for _ in range(N):
    action = sys.stdin.readline().split()
    act = action[0]

    if act == 'push':
        stack.append(action[1])
        top += 1
    elif act == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack.pop())
            top -= 1
    elif act == 'size':
        print(top + 1)
    elif act == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif act == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])