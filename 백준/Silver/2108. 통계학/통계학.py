import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

print(round(sum(nums)/N))

lst = sorted(nums)
print(lst[len(lst)//2])

nums.sort()
# nums 리스트 하나씩 카운트 해서, 가장 많이 나온 두개 숫자 뽑기
# most_common 하면 튜플 형태로,  /  안하면 딕셔너리처럼 나온다
ans = Counter(nums).most_common(2)
if len(ans) > 1:
    if ans[0][1] == ans[1][1]:
        print(ans[1][0])
    else:
        print(ans[0][0])
else:
    print(ans[0][0])

print(max(nums) - min(nums))