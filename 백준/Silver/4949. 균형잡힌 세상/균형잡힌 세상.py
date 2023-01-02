import sys

input = sys.stdin.readline


while True:
    stack = []
    isOK = True
    s = input().rstrip()
    if s == '.':
        break
    for j in s:
        if j == '(':
            stack.append(j)
        elif j == '[':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0 or stack[-1] == '[':
                isOK = False
                break
            else:
                stack.pop()
        elif j == ']':
            if len(stack) == 0 or stack[-1] == '(':
                isOK = False
                break
            else:
                stack.pop()

    if not isOK or len(stack) != 0:
        print('no')
    else:
        print('yes')
