import sys

def is_prime(num):
    for i in range(2, int((2 * n) ** 0.5) + 1):
        if num % i == 0:
            prime_dic[num] = 0
            return 0
    prime_dic[num] = 1
    return 1

prime_dic = {}

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    ans = 0
    for num in range(n+1, (2*n)+1):
        if num in prime_dic.keys():
            ans += prime_dic[num]
        else:
            ans += is_prime(num)
    print(ans)