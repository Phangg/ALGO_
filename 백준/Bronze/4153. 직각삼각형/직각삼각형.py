import sys

while 1:
    nums = list(map(int, sys.stdin.readline().split()))
    if nums == [0, 0, 0]:
        break
    nums.sort()
    if max(nums)**2 == (nums[0]**2) + (nums[1]**2):
        print('right')
    else:
        print('wrong')