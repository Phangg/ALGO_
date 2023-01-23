import sys

# n : 원생 수 / k : 조 개수
# tall_lst : 원생들의 키 리스트
n, k = map(int, sys.stdin.readline().split())
tall_lst = list(map(int, sys.stdin.readline().split()))

# lst : 인접한 원생들의 키 차이를 담은 리스트
lst = []
for i in range(1, n):
    lst.append(tall_lst[i] - tall_lst[i-1])

lst.sort(reverse=True)

# 최소 비용 구하기
print(sum(lst[k-1:]))