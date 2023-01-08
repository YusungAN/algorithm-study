import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split(' '))
li = []
for _ in range(n):
    li.append(list(map(int, list(input().rstrip()))))

zeros = [[0]*m for _ in range(n)]
zeros_cnt = [0]*500001
idx = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x, y):
    global idx
    q = deque()
    q.append((x, y))
    zeros[y][x] = idx
    zeros_cnt[idx] += 1
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            mx = nx + dx[i]
            my = ny + dy[i]
            if 0 <= mx < m and 0 <= my < n and zeros[my][mx] == 0 and li[my][mx] == 0:
                q.append((mx, my))
                zeros[my][mx] = idx
                zeros_cnt[idx] += 1


for i in range(n):
    for j in range(m):
        if li[i][j] == 0 and zeros[i][j] == 0:
            bfs(j, i)
            idx += 1

for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            near = set()
            for k in range(4):
                mx = j + dx[k]
                my = i + dy[k]
                if 0 <= mx < m and 0 <= my < n and li[my][mx] == 0:
                    near.add(zeros[my][mx])
            for k in list(near):
                li[i][j] += zeros_cnt[k]
                li[i][j] %= 10

for i in li:
    for j in i:
        print(j, end='')
    print('')

