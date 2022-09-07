import sys

def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

M, N = map(int, sys.stdin.readline().split())    
    
for num in range(M, N+1):
    if is_prime(num):
        print(num)
        
# lst = list(range(M, N+1))
# if M == 1:
#     lst.remove(M)
# elif M >= 2:
#     for num in range(M, N+1):
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 lst.remove(num)
#                 break
# for ans in lst:
#     print(ans)