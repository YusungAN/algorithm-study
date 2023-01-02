import sys

input = sys.stdin.readline

N = int(input())
res = 0
stack = []
for i in range(N):
    s = input().rstrip()
    if len(s) > 1:
        f, a, t = map(int, s.split(' '))
        if t == 1:
            res += a
        else:
            stack.append((a, t-1))
    else:
        if len(stack) > 0:
            aa, tt = stack.pop()
            if tt == 1:
                res += aa
            else:
                stack.append((aa, tt-1))

print(res)