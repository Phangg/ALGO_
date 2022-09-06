N, k = map(int, input().split())

nums = list(map(int, input().split()))

lst = sorted(nums)
print(lst[N-k])