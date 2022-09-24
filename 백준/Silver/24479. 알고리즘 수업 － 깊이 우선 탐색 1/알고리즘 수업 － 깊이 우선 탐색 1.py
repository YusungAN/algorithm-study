import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split(' '))
visited = [False]*(n+1)
dic = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split(' '))
    dic[a].append(b)
    dic[b].append(a)

cnt = 0
res = [0]*(n+1)
def dfs(r):
    global cnt
    visited[r] = True
    cnt += 1
    res[r] = cnt
    dic[r].sort()
    isok = False
    for i in dic[r]:
        if not visited[i]:
            isok = True
            dfs(i)
    if not isok:
        return

dfs(r)

for i in res[1:]:
    print(i)