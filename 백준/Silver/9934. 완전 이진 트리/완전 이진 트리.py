import sys
from collections import defaultdict

def node(k, lst):
    global dic
    if k > 1:
        c = ((2**k)-1)//2
        dic[k].append(lst[c])
        node(k-1, lst[:c])
        node(k-1, lst[c+1:])
    else:
        dic[k].append(lst[0])


K = int(sys.stdin.readline())
build = list(map(int, sys.stdin.readline().split()))

dic = defaultdict(list)
node(K, build)

for ans in dic.values():
    print(*ans)