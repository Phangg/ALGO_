import sys
N = int(sys.stdin.readline())

lst = [0]* 10001

for _ in range(N):
    num = int(sys.stdin.readline()) 
    lst[num] += 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)

