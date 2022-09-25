import sys
from collections import defaultdict


input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, list(input().rstrip()))))

res = []
cnt = 0
def dfs(x, y):
    global cnt
    li[y][x] = 0
    #print('asdf')
    cnt += 1
    isok = False
    if y > 0 and li[y-1][x] == 1:
        isok = True
        dfs(x, y-1)
    if x > 0 and li[y][x-1] == 1:
        isok = True
        dfs(x-1, y)
    if y < n-1 and li[y+1][x] == 1:
        isok = True
        dfs(x, y+1)
    if x < n-1 and li[y][x+1] == 1:
        isok = True
        dfs(x+1, y)
    if not isok:
        return

for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            dfs(j, i)
            res.append(cnt)
            cnt = 0

print(len(res))
res.sort()
for i in res:
    print(i)