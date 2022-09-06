import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

N = int(sys.stdin.readline())
ring = list(map(int, input().split()))

for i in range(1, N):
    a = ring[0]//gcd(ring[0], ring[i])
    b = ring[i]//gcd(ring[0], ring[i])
    print(f'{a}/{b}')