result = 0

while True:

    A,B = map(int, input().split())
    result = A + B 
    if result == 0:
        break
    print(result)