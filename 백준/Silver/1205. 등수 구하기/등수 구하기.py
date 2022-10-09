import sys

N, T, P = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

if N >= P and T <= num[-1]:
    print(-1)
    exit()
elif N <= P:
    if T in num:
        print(num.index(T)+1)
    else:
        num.append(T)
        num.sort(reverse=True)
        print(num.index(T)+1)