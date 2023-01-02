import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split(' '))
q = deque(list(range(1, n+1)))
res = []
while len(q) > 0:
    for i in range(k-1):
        q.append(q.popleft())
    res.append(q.popleft())

print('<', end='')
for i in range(len(res)):
    print(res[i], end='')
    if i != len(res)-1:
        print(', ', end='')
print('>')