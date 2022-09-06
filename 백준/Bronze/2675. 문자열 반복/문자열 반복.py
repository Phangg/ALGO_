T = int(input())

for tc in range(T):
    n, s = map(str, input().split())
    for i in s:
        print(i*int(n), end='')
    print()