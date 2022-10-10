import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))
s = list(map(int, input().rstrip()))
stack = []
pop_cnt = 0
for i in s:
    while len(stack) != 0 and stack[-1] < i and pop_cnt < k:
        stack.pop()
        pop_cnt += 1
    stack.append(i)

while pop_cnt < k:
    stack.pop()
    pop_cnt += 1
for i in stack:
    print(i, end='')
