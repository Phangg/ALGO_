import sys

sen = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())

stack = []
for s in sen:
    stack.append(s)
    if len(stack) < len(bomb):
        continue
    while stack[-len(bomb):] == bomb:
        del stack[-len(bomb):]
if stack:
    print(''.join(stack))
else:
    print('FRULA')