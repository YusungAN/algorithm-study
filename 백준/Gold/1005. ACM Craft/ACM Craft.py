import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    w = list(map(int, input().split(' ')))
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n + 1)]
    indeg = [0]*(n+1)
    for i in range(k):
        a, b = map(int, input().split(' '))
        graph[a].append(b)
        reverse_graph[b].append(a)
        indeg[b] += 1
    h = int(input())
    q = deque()
    ans = 0
    dp = [0]*(n+1)
    flag = False
    for i in range(1, n+1):
        if indeg[i] == 0:
            if i == h:
                flag = True
                break
            q.append(i)
            dp[i] = w[i-1]
    if flag:
        print(w[h-1])
        continue
    while q:
        now = q.popleft()
        if now == h:
            break
        tmp = 0
        for next in graph[now]:
            if indeg[next] > 0:
                indeg[next] -= 1
                dp[next] = max(dp[next], dp[now]+w[next-1])
            if indeg[next] == 0:
                q.append(next)
    print(dp[h])
