import sys

input = sys.stdin.readline

n = int(input())
li = []
visited = [True]+[False for i in range(n-1)]
for i in range(n):
    li.append(list(map(int, input().split(' '))))


def calc():
    a = 0
    b = 0
    for i in range(n):
        for j in range(i+1, n):
            if visited[i] and visited[j]:
                a += li[i][j]+li[j][i]
            elif not visited[i] and not visited[j]:
                b += li[i][j]+li[j][i]

    return abs(a-b)


_min = 1e9


def dfs(depth, idx):
    global _min
    if depth == n // 2:
        _min = min(_min, calc())
        return
    for i in range(idx, n):
        if visited[i]:
            continue
        visited[i] = True
        dfs(depth+1, i+1)
        visited[i] = False




dfs(1, 1)
print(_min)