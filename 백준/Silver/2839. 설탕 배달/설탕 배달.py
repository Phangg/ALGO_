N = int(input())

m = 0
while N >= 0:
    if N % 5 == 0:
        m += (N//5)
        print(m)
        break
    else:
        N -= 3
        m += 1
else:
    print(-1)