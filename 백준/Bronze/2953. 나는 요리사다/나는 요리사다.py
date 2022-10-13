max_v = 0
who = 0
for i in range(5):
    x = sum(list(map(int, input().split())))
    if max_v < x:
        max_v = x
        who = i+1
print(who, max_v)