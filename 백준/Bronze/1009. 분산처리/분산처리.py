import sys
from collections import defaultdict

num_dict = defaultdict(list)
i = 1
num_dict[0].append(10)
for x in range(1, 10):
    data = x
    num_dict[x].append(data)
    while 1:
        data = (data * x) % 10
        if data not in num_dict[x]:
            num_dict[x].append(data)
        else:
            break
        i += 1

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10

    tmp = num_dict[a]
    res = tmp[(b % len(tmp))-1]
    print(res)