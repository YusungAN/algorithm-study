import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
q = deque([])

for i in range(t):
    s = input()
    if s[0:9] == 'push_back':
        q.append(int(s[10:]))
    elif s[0:9] == 'push_fron':
        q.appendleft(int(s[10:]))
    elif s[0:8] == 'pop_back':
        print(q.pop() if len(q) > 0 else -1)
    elif s[0:8] == 'pop_fron':
        print(q.popleft() if len(q) > 0 else -1)
    elif s[0] == 's':
        print(len(q))
    elif s[0] =='e':
        print(0 if len(q) != 0 else 1)
    elif s[0] == 'f':
        print(q[0] if len(q) > 0 else -1)
    elif s[0] == 'b':
        print(q[-1] if len(q) > 0 else -1)