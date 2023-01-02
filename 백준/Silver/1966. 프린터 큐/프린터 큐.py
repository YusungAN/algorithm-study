import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split(' '))
    q = deque(list(map(int, input().split(' '))))

    cnt = 1
    while len(q) > 0:
        if len(q) == 1:
            print(cnt)
            break
        if q[0] >= max(q):
            q.popleft()
            if 0 == m:
                print(cnt)
                break
            cnt += 1
            m -= 1
        else:
            q.append(q.popleft())
            if m == 0:
                m = len(q)-1
            else:
                m -= 1
