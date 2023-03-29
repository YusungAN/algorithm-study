import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    s, num = input().rstrip().split()
    li.append(list(s)+[int(num)])

li.append(list(map(int, input().split()))+[-1])

w = [[1]*n+[0] for _ in range(n)]
w.append([0]*(n+1))

for i in range(n):
    for j in range(n):
        if li[i][j] == 'R':
            w[i][j+1] += w[i][j]
        else:
            w[i+1][j] += w[i][j]
# print(w)
ans = 0
for i in range(n):
    ans += li[n][i]*w[n][i]
    ans += li[i][n]*w[i][n]
print(ans)

def dfs(x, y, update):
    if x < n and li[y][x] == 'R':
        w[y][x+1] += update
        dfs(x+1, y, update)
    elif y < n and li[y][x] == 'D':
        w[y+1][x] += update
        dfs(x, y+1, update)

for _ in range(int(input())):
    y, x = map(int, input().split(' '))
    x -= 1
    y -= 1
    dfs(x, y, -w[y][x])
    # print(w, li)
    li[y][x] = 'D' if li[y][x] == 'R' else 'R'
    dfs(x, y, w[y][x])
    # print(w, li)
    ans = 0
    for i in range(n):
        ans += li[n][i] * w[n][i]
        ans += li[i][n] * w[i][n]
    print(ans)
