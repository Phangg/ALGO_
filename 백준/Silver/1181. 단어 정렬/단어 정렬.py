import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(N)]
words = list(set(words))

words.sort(key=lambda x: (len(x), x))

for ans in words:
    print(ans)