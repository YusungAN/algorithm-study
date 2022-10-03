import sys

input = sys.stdin.readline

stack = [(0, 0)]
max_area = 0
x_cnt = 0
n = int(input())
for i in range(1, n+1):
    a = int(input())
    if i == 1:
        stack.append((i, a))
        continue
    check = (0, 0)
    while stack[-1][1] > a:
        check = stack.pop()
        max_area = max(max_area, check[1]*(i-stack[-1][0]-1))
    stack.append((i, a))
    if i == n:
        while len(stack) > 1:
            check = stack.pop()
            max_area = max(max_area, check[1] * (i - stack[-1][0]))

print(max_area)