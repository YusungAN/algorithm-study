import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, r, q = map(int, input().split(' '))

tree = [[] for _ in range(n+1)]
dp = [0]*(n+1)

for _ in range(n-1):
    u, v = map(int, input().split(' '))
    tree[u].append(v)
    tree[v].append(u)
    dp[u] += 1
    dp[v] += 1

def dfs(cur, parent):
    dp[cur] = 1
    for i in tree[cur]:
        if i != parent:
            dp[cur] += dfs(i, cur)
    return dp[cur]

dfs(r, r)

for _ in range(q):
    print(dp[int(input())])
