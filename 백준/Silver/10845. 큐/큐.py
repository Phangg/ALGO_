import sys
from collections import deque

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다

N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    go = sys.stdin.readline().rstrip()
    
    if ' ' in go:
        og, num = go.split(' ')
        q.append(num)
    elif go == 'pop':
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif go == 'size':
        print(len(q))
    elif go == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif go == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif go == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
