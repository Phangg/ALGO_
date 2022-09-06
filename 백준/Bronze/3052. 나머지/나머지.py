lst = []

for i in range(10):
    n = int(input())
    lst.append(n % 42)

print(len(set(lst)))