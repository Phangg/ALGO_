n, l, d = map(int, input().split())
all = ((n-1)*5) + (n*l)
s = [0] * all
for i in range(0, all, l+5):
    for j in range(i, i+l):
        s[j] = 1
for i in range(0, all, d):
    if not s[i]:
        print(i)
        break
else:
    print(i + d)