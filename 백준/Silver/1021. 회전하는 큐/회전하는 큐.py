import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split(' '))
q = deque(list(range(1, n+1)))

li = list(map(int, input().split(' ')))

cnt = 0
for i in li:
    if q.index(i) <= len(q)//2:
        while q[0] != i:
            q.append(q.popleft())
            cnt += 1
            # print(q)
        q.popleft()
        # print(q)
    else:
        while q[0] != i:
            q.appendleft(q.pop())
            cnt += 1
            # print(q)
        q.popleft()
        # print(q)

print(cnt)



