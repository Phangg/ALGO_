perfect = [1, 1, 2, 2, 2, 8]

mine = list(map(int, input().split()))

lst = []
for i, v in enumerate(perfect):
    lst.append(v - mine[i])

for j in lst:
    print(j, end=' ')