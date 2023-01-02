import sys
from collections import deque

input = sys.stdin.readline

q = deque([])
n = int(input())

for i in range(n):
    s = input()

    if s[0:2] == 'pu':
        i = int(s[5:])
        q.append(i)
    elif s[0] == 'p':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif s[0] == 's':
        print(len(q))
    elif s[0] == 'e':
        print(1 if len(q) == 0 else 0)
    elif s[0] == 'f':
        print(q[0] if len(q) > 0 else -1)
    elif s[0] == 'b':
        print(q[-1] if len(q) > 0 else -1)