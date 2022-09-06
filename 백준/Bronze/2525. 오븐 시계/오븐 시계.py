H,M = map(int, input().split())
run_M = int(input())

M += run_M

if M >= 60:
    d,m = divmod(M, 60)
    H += d
    M = m

if H >= 24:
    H -= 24

print(H,M)
