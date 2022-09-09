import sys

while 1:
    sen = list(map(str, sys.stdin.readline().rstrip()))
    if sen[0] == '.':
        break

    stack = []
    for char in sen:
        if len(stack) == 0:
            if char == '(' or char == '[':
                stack.append(char)
            elif char == ')' or char == ']':
                stack.append(char)
                break
        elif stack[-1] == '(':
            if char == ']':
                stack.append(char)
                break
            elif char == ')':
                stack.pop()
            elif char == '(' or char == '[':
                stack.append(char)
        elif stack[-1] == '[':
            if char == ')':
                stack.append(char)
                break
            elif char == ']':
                stack.pop()
            elif char == '(' or char == '[':
                stack.append(char)
    if stack:
        print('no')
    else:
        print('yes')