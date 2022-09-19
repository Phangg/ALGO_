import sys

M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    order = sys.stdin.readline().rstrip()
    if ' ' in order:
        og, n = order.split()
        n = int(n)
        if og == 'add':
            S.add(n)
        elif og == 'remove':
            if n in S:
                S.remove(n)
        elif og == 'check':
            if n in S:
                print(1)
            else:
                print(0)
        elif og == 'toggle':
            if n in S:
                S.remove(n)
            else:
                S.add(n)
    elif order == 'all':
        S = set(range(1, 21))
    elif order == 'empty':
        S.clear()
