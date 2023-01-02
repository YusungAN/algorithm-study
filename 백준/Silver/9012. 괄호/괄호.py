import sys

input = sys.stdin.readline

T = int(input())
stack = []

for i in range(T):
    um = False
    s = input().rstrip()
    stack = []
    for j in range(len(s)):
        if len(stack) == 0 and s[j] == ')':
            um = True
            break
        if j > 0 and s[j] == ')':
            stack.pop()
        else:
            stack.append(s[j])
    if len(stack) == 0 and not um:
        print('YES')
    else:
        print('NO')