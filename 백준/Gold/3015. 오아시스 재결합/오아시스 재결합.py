import sys

input = sys.stdin.readline

stack = []
cnt = 0
n = int(input())
for _ in range(n):
    a = int(input())
    while len(stack) > 0 and a > stack[-1][0]:
        cnt += stack[-1][1]
        stack.pop()
    if len(stack) == 0:
        stack.append((a, 1))
        continue
    temp_cnt = 0
    if stack[-1][0] == a:
        temp_cnt = stack.pop()[1]
        cnt += temp_cnt
        if len(stack) > 0:
            cnt += 1
        stack.append((a, temp_cnt+1))
    else:
        stack.append((a, 1))
        cnt += 1



print(cnt)
