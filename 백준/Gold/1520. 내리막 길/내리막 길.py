import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

m, n = map(int, input().split(' '))
li = []
for i in range(m):
    li.append(list(map(int, input().split(' '))))

dp = [[-1]*n for _ in range(m)]


def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    cnt = 0
    if x > 0 and li[y][x-1] < li[y][x]:
        cnt += dfs(x-1, y)
    if y > 0 and li[y][x] > li[y-1][x]:
        cnt += dfs(x, y-1)
    if x < n-1 and li[y][x] > li[y][x+1]:
        cnt += dfs(x+1, y)
    if y < m-1 and li[y][x] > li[y+1][x]:
        cnt += dfs(x, y+1)

    dp[y][x] = cnt
    return cnt


print(dfs(0, 0))
