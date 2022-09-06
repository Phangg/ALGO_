N = int(input())

num = N
cycle_cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    cycle_cnt += 1

    if num == N:
        break
print(cycle_cnt)
