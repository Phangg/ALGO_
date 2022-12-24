import sys

# s : 문자열
s = sys.stdin.readline().strip()

for i in range(len(s)):
    # 뒤집은거랑 같을 때,
    if s[i:] == s[i:][::-1]:
        print(len(s) + i)
        break