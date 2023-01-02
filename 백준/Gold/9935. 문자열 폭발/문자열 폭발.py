import sys

input = sys.stdin.readline

s = list(input().rstrip())
boom = list(input().rstrip())
boomlen = len(boom)
stack = []
top = -1
for i in s:
    stack.append(i)
    top += 1
    if top+1 >= boomlen and stack[top-boomlen+1:top+1] == boom:
        for j in range(boomlen):
            stack.pop()
            top -= 1

if len(stack) == 0:
    print('FRULA')
else:
    for i in stack:
        print(i, end='')

