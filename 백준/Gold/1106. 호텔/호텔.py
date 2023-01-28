import sys

# c : 고객을 적어도 c 명으로 만들어야 함 / n : 도시 개수
# lst : [도시에 홍보할 때 대는 비용, 그 비용으로 얻을 수 있는 고객의 수] 를 담은 2차원 리스트
c, n = map(int, sys.stdin.readline().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

# 비용 기준 정렬
lst_sort = sorted(lst, key=lambda x: x[0])

# 최소 비용
# p <= 100 and c를 넘기더라도 최소비용을 찾기 때문!
min_m = [float('inf')] * (c + 101)
min_m[0] = 0

# m : 비용 / p : 고객
for m, p in lst_sort:
    # p <= 100 and c를 넘기더라도 최소비용을 찾기 때문!
    for i in range(p, c + 101):
        min_m[i] = min(min_m[i - p] + m, min_m[i])

print(min(min_m[c:]))