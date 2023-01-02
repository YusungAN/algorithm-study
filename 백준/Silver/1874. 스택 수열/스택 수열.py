import sys

input = sys.stdin.readline

n = int(input())
stack = []
seq = []
for i in range(n):
    seq.append(int(input()))

res = []
idx = 0
i = 1
isOK = True
while i <= n or len(stack) > 0:
    if i == n+1 and stack[-1] != seq[idx]:
        isOK = False
        break
    if len(stack) > 0 and stack[-1] == seq[idx]:
        stack.pop()
        idx += 1
        res.append('-')
    else:
        stack.append(i)
        res.append('+')
        i += 1


if isOK:
    for i in res:
        print(i)
else:
    print('NO')
