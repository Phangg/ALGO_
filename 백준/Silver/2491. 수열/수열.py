import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

stack = []
stack.append(nums[0])                           # 리스트의 처음 값으로 시작
add_ans = 0                                     # 제일 크게 카운트 된 숫자 저장
add_cnt = 1                                     # 연속되는 숫자 개수 카운트
for i in range(1, N):
    if stack[-1] <= nums[i]:                    # 같거나, 연속해서 커지는 경우
        stack.append(nums[i])
        add_cnt += 1
    else:
        stack.clear()
        add_ans = max(add_ans, add_cnt)
        stack.append(nums[i])
        add_cnt = 1                             # 스택 비우고 , 최대값 체크 , 현재 값 스택 삽입 , 카운트 1 초기화
add_ans = max(add_ans, add_cnt)

stack = []
stack.append(nums[0])
sub_ans = 0
sub_cnt = 1
for j in range(1, N):
    if nums[j] <= stack[-1]:                    # 같거나, 연속해서 작아지는 경우
        stack.append(nums[j])
        sub_cnt += 1
    else:
        stack.clear()
        sub_ans = max(sub_ans, sub_cnt)
        stack.append(nums[j])                   # 스택 비우고 , 최대값 체크 , 현재 값 스택 삽입 , 카운트 1 초기화
        sub_cnt = 1
sub_ans = max(sub_ans, sub_cnt)

res = max(add_ans, sub_ans)
print(res)