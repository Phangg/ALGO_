import sys
from collections import defaultdict

t = int(sys.stdin.readline())
for _ in range(t):
    dic = defaultdict(int)

    N = int(sys.stdin.readline())
    n_note = sorted(set(map(int, sys.stdin.readline().split())))
    for n in n_note:
        dic[n] = 1

    M = int(sys.stdin.readline())
    m_note = list(map(int, sys.stdin.readline().split()))
    for m in m_note:
        print(dic[m])
