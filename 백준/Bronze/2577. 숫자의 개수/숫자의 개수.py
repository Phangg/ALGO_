A = int(input())
B = int(input())
C = int(input())

total = str(A*B*C)

for i in range(0,10):
    result = total.count(str(i))
    print(result)