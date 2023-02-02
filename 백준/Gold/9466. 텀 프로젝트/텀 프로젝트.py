import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    li = [0]+list(map(int, input().split(' ')))
    visited = [False]*(n+1)
    inner_visited = [False] * (n + 1)
    cnt = 0
    for i in range(1, n+1):
        def dfs(k):
            global cnt
            visited[k] = True
            next = li[k]
            if not visited[next]:
                dfs(next)
            elif not inner_visited[next]:
                idx = next
                cnt += 1
                while idx != k:
                    idx = li[idx]
                    cnt += 1
            inner_visited[k] = True
        if not visited[i]:
            dfs(i)

    print(n-cnt)
