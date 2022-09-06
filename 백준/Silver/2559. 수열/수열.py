import sys
def min_temp(x: list, n, k):
    max_t = sum(x[:k])
    s = sum(x[:k])
    for i in range(n - k):
        s = s - (x[i]) + (x[i+k])
        if max_t < s:
            max_t = s
    return max_t

# N : 전체 날짜 수 / K : 연속적인 날짜 수 / temp_lst : N일간 온도 리스트 (N개의 숫자)
N, K = map(int, sys.stdin.readline().split())
temp_lst = list(map(int, sys.stdin.readline().split()))

print(min_temp(temp_lst, N, K))