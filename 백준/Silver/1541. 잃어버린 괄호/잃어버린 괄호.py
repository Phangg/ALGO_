import sys

modify = list(sys.stdin.readline().split('-'))

nums = []
for m in modify:
    tmp = m.split('+')
    x = 0
    for n in tmp:
        x += int(n)
    nums.append(x)

ans = nums[0]
for i in range(1, len(nums)):
    ans -= nums[i]
print(ans)