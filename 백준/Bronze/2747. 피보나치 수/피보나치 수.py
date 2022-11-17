f = [0] * 50
x = int(input())
f[0], f[1] = 0, 1
for i in range(2, x+1):
    f[i] = f[i-1] + f[i-2]
print(f[x])