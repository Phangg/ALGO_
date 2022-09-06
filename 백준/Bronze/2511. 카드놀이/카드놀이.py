import sys

a_score = list(map(int, sys.stdin.readline().split()))
b_score = list(map(int, sys.stdin.readline().split()))

A, B, D = 0, 0, 0
lst = []
for score in range(10):
    if a_score[score] > b_score[score]:
        A += 3
        lst.append('A')
    elif a_score[score] < b_score[score]:
        B += 3
        lst.append('B')
    else:
        A += 1
        B += 1
        D += 1

if A > B:
    print(A, B)
    print('A')
elif A < B:
    print(A, B)
    print('B')
elif D == 10:
    print(A, B)
    print('D')
else:
    print(A, B)
    print(lst[-1])