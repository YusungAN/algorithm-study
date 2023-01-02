import sys

input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    s = input()
    if s[0:2] == 'pu':
        stack.append(int(s[5:]))
    elif s[0:2] == 'po':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print('-1')
    elif s[0] == 't':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print('-1')
    elif s[0] == 's':
        print(len(stack))
    else:
        if len(stack) == 0:
            print('1')
        else:
            print('0')