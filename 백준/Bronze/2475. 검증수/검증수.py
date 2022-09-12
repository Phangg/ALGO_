import sys

lst = list(map(int, sys.stdin.readline().split()))
num = 0
for i in lst:
    num += (i**2)
print(num%10)