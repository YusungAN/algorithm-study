import sys

input = sys.stdin.readline

K = int(input())
stack = []

for i in range(K):
    a = int(input())
    if a == 0:
        stack.pop()
        continue
    stack.append(a)

print(sum(stack))