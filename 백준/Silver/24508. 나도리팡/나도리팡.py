import sys

# n 개의 바구니
# k 마리가 되면 터짐
# t 회 반복 가능
# nadori : 각 바구니에 담긴 나도리의 개수 리스트
n, k, t = map(int, sys.stdin.readline().split())
nadori = sorted(list(map(int, sys.stdin.readline().split())))

# no_zero : 0이 아닌 바구니 수
no_zero = n - nadori.count(0)

if no_zero == 0:
    print('YES')
    exit()

elif no_zero == 1:
    print('NO')
    exit()

nadori.sort()

# s : 제일 작은 숫자 바구니 인덱스
# e : 제일 큰 숫자 바구니 인덱스
s = n - no_zero
e = n - 1

while t > 0 and s < e:
    # need : '나도리 팡' 을 위해 필요한 나도리 숫자
    need = k - nadori[e]

    if nadori[s] < need:
        nadori[e] += nadori[s]
        t -= nadori[s]
        s += 1

    else:
        nadori[e] += need
        nadori[s] -= need
        t -= need
        e -= 1
        if nadori[s] == 0:
            s += 1

if s > e and t >= 0:
    print('YES')
else:
    print('NO')